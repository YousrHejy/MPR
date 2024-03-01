import vtk

def readFiles(filename):
    readDICOM = vtk.vtkMetaImageReader()
    readDICOM.SetFileName(filename)
    readDICOM.Update()
    image = readDICOM.GetOutput()
    dimensions = image.GetDimensions()
    scalarRange = image.GetScalarRange()
    return dimensions, scalarRange, image
def mainWindow():
    # Define main renderer window
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetSize(1000, 1000)
    renderWindow.BordersOn()
    return renderWindow
def interaction(window):
    # Define interactor and interactor style
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowStyle = vtk.vtkInteractorStyleTrackballCamera()
    renderWindowInteractor.SetInteractorStyle(renderWindowStyle)
    # define selected scene for interacrion
    renderWindowInteractor.SetRenderWindow(window)
    picker = vtk.vtkCellPicker()
    picker.SetTolerance(0.005)
    renderWindowInteractor.SetPicker(picker)
    renderWindowInteractor.GetPickingManager().SetEnabled(1)
    renderWindowInteractor.GetPickingManager().AddPicker(picker)
    renderWindowInteractor.Initialize()
    return renderWindowInteractor
def createRenders(xmin,ymin,xmax,ymax,renderWindow,renders):
    render = vtk.vtkRenderer()
    renderWindow.AddRenderer(render)
    render.SetViewport(xmin, ymin, xmax, ymax)
    renders.append(render)

if __name__ == "__main__":
    # thresholds for volume rendering
    thresh1 = 150
    thresh2 = 320
    thresh3 = 440
    # no of slices
    # # Define viewport ranges in renderwindow
    xmins = [0, 0.51, 0, 0.51]
    xmaxs = [0.49, 1, 0.49, 1]
    ymins = [0, 0, 0.51, 0.51]
    ymaxs = [0.49, 0.49, 1, 1]
    dimensionsNumber = 3
    wholeExtent, scalarRange, myMHD = readFiles("out.mhd")
    renderWindow = mainWindow()
    renderWindowInteractor = interaction(renderWindow)
    # # TODO : confirm if this camera orientation is good for 3D echo
    viewUp = [[0, 0, -1], [0, 0, -1], [0, 1, 0]]
    # # Define 3 MPR views using image plane widgets and reslice cursor
    ipws = []
    renders = []
    rcws = []
    rcwReps = []
    # First renderer, used to display volume3D or slice planes in 3D
    createRenders(xmins[3], ymins[3], xmaxs[3], ymaxs[3], renderWindow, renders)
    # Reslice cursor generating the 3 slice planes
    resliceCursor = vtk.vtkResliceCursor()
    resliceCursor.SetCenter(myMHD.GetCenter())
    resliceCursor.SetImage(myMHD)
    # # Enable the cursor by default
    for i in range(dimensionsNumber):
        createRenders(xmins[i], ymins[i], xmaxs[i], ymaxs[i], renderWindow, renders)
        # One vtkResliceCursorWidget for each slice orientation, based on common Reslice cursor
        rcwRep = vtk.vtkResliceCursorThickLineRepresentation()
        rcwRep.SetRestrictPlaneToVolume(1)
        rcwReps.append(rcwRep)
        rcwRep.GetResliceCursorActor().GetCursorAlgorithm().SetResliceCursor(
            resliceCursor
        )
        renders[i+1].AddActor(rcwRep.GetResliceCursorActor().GetCursorAlgorithm().SetReslicePlaneNormal(i))
        rcwRep.ManipulationMode = 3
        rcw = vtk.vtkResliceCursorWidget()
        rcws.append(rcw)
        rcw.SetInteractor(renderWindowInteractor)
        rcw.SetRepresentation(rcwRep)
        rcw.SetDefaultRenderer(renders[i+1])
        rcw.SetEnabled(1)
        # Setting right camera orientation
        renders[i+1].GetActiveCamera().SetFocalPoint(0, 0, 0)
        camPos = [0, 0, 0]
        camPos[i] = 1
        renders[i+1].GetActiveCamera().SetPosition(camPos)
        renders[i+1].GetActiveCamera().ParallelProjectionOn()
        renders[i+1].GetActiveCamera().SetViewUp(viewUp[i])
        renders[i+1].ResetCamera()
        # Initialize the window level to a sensible value
        rcwRep.SetWindowLevel(
            scalarRange[1] - scalarRange[0], (scalarRange[0] + scalarRange[1]) / 2.0
        )
    #     # Make all slice plane share the same color map.
        rcwRep.SetLookupTable(rcwReps[0].GetLookupTable())
    #
        rcw.On()
    # # 3D Raycast Viewer
    colorTransferFunction = vtk.vtkColorTransferFunction()
    colorTransferFunction.AddRGBPoint(scalarRange[0], 0.0, 0.0, 0.0)
    colorTransferFunction.AddRGBPoint(thresh1, 100 / 255, 64 / 255, 38 / 255)
    colorTransferFunction.AddRGBPoint(thresh2, 225 / 255, 154 / 255, 74 / 255)
    colorTransferFunction.AddRGBPoint(thresh3, 255 / 255, 239 / 255, 243 / 255)
    colorTransferFunction.AddRGBPoint(scalarRange[1], 211 / 255, 168 / 255, 255 / 255)

    funcOpacityScalar = vtk.vtkPiecewiseFunction()
    funcOpacityScalar.AddPoint(scalarRange[0], 0)
    funcOpacityScalar.AddPoint(thresh1, 0)
    funcOpacityScalar.AddPoint(thresh2, 0.45)
    funcOpacityScalar.AddPoint(thresh3, 0.63)
    funcOpacityScalar.AddPoint(scalarRange[1], 0.63)

    volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
    volumeMapper.SetInputData(myMHD)
    volumeMapper.SetBlendModeToComposite()
    volumeMapper.AutoAdjustSampleDistancesOn()

    volumeProperty = vtk.vtkVolumeProperty()
    volumeProperty.ShadeOn()
    volumeProperty.SetScalarOpacity(funcOpacityScalar)
    volumeProperty.SetInterpolationTypeToLinear()
    volumeProperty.SetColor(colorTransferFunction)
    volumeProperty.SetAmbient(0.20)
    volumeProperty.SetDiffuse(1.00)
    volumeProperty.SetSpecular(0.00)
    volumeProperty.SetSpecularPower(0.00)

    actorVolume = vtk.vtkVolume()
    actorVolume.SetMapper(volumeMapper)
    actorVolume.SetProperty(volumeProperty)  # Define renderer for Volume

    renders[0].SetBackground(255 / 255, 255 / 255, 255 / 255)
    renders[0].AddVolume(actorVolume)
    renders[0].ResetCameraClippingRange()
    #
    renderWindow.Render()
    renderWindowInteractor.Start()
