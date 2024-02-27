from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence
from PySide6.QtUiTools import QUiLoader
import vtkmodules.all as vtk

# from TreePointLists import TreePointLists
# from SegmentationList import SegmentationList
# from CommandSliceSelect import CommandSliceSelect
# from CommandSegment import CommandSegment
# from SegmentationImage import SegmentationImage


import sys


class OrthoViewer(QMainWindow):
    def __init__(self, parent=None):
        super(OrthoViewer, self).__init__(parent)
        self.loader = QUiLoader()
        self.ui = self.loader.load("uiOrthoViewer.ui", self)
        self.setCentralWidget(self.ui)

        # additional UI stuff
        # self.treePointLists = TreePointLists(self.ui.pagePointLists)
        self.ui.gridLayout_3.addWidget(self.treePointLists)
        self.treePointLists.setVisible(True)

        # self.segmentationList = SegmentationList(self.ui.pageSegmentationList)
        self.segmentationList.setVisible(True)

        # vtk stuff
        self.vecRenderer = []
        self.imageReader = vtk.vtkMetaImageReader()
        self.imageReader.SetFileName("C:\\Temp\\out.mhd")
        self.imageReader.UpdateWholeExtent()

        print(self.imageReader.GetAnatomicalOrientation())

        image_range = self.imageReader.GetOutput().GetScalarRange()
        self.imageShiftScale = vtk.vtkImageShiftScale()
        self.imageShiftScale.SetInputConnection(self.imageReader.GetOutputPort())
        self.imageShiftScale.SetOutputScalarTypeToUnsignedChar()
        self.imageShiftScale.SetShift(-image_range[0])
        self.imageShiftScale.SetScale(255.0 / (image_range[1] - image_range[0]))
        self.imageShiftScale.UpdateWholeExtent()

        self.imageWindowLevel = vtk.vtkImageMapToWindowLevelColors()
        self.imageWindowLevel.SetInputConnection(self.imageShiftScale.GetOutputPort())
        self.imageWindowLevel.SetWindow(100.0)
        self.imageWindowLevel.SetLevel(50.0)
        self.imageWindowLevel.UpdateWholeExtent()

        self.imageMapToColors = vtk.vtkImageMapToColors()
        self.imageMapToColors.SetOutputFormatToRGBA()
        self.imageMapToColors.SetInputConnection(self.imageWindowLevel.GetOutputPort())
        self.grayscaleLut = vtk.vtkLookupTable()
        self.grayscaleLut.SetNumberOfTableValues(256)
        self.grayscaleLut.SetTableRange(0, 255)
        self.grayscaleLut.SetRampToLinear()
        self.grayscaleLut.SetHueRange(0, 0)
        self.grayscaleLut.SetSaturationRange(0, 0)
        self.grayscaleLut.SetValueRange(0, 1)
        self.grayscaleLut.SetAlphaRange(1, 1)
        self.grayscaleLut.Build()
        self.imageMapToColors.SetLookupTable(self.grayscaleLut)
        self.imageMapToColors.UpdateWholeExtent()

        self.segmentationImage = vtk.vtkImageData()
        self.segmentationImage.DeepCopy(self.imageShiftScale.GetOutput())
        sz = (
            self.segmentationImage.GetDimensions()[0]
            * self.segmentationImage.GetDimensions()[1]
            * self.segmentationImage.GetDimensions()[2]
        )
        pt = vtk.util.numpy_support.vtk_to_numpy(
            self.segmentationImage.GetScalarPointer()
        )
        pt.fill(0)
        self.segmentationImage.Update()

        self.segmentationLabelImage = vtk.vtkImageMapToColors()
        self.segmentationLabelImage.SetInputData(self.segmentationImage)
        self.segmentationLabelImage.SetOutputFormatToRGBA()
        self.segmentationLabelLookupTable = vtk.vtkLookupTable()
        self.segmentationLabelLookupTable.SetNumberOfTableValues(256)
        self.segmentationLabelLookupTable.SetTableRange(0, 255)
        self.segmentationLabelLookupTable.SetTableValue(0, 0, 1, 0, 0.0)
        self.segmentationLabelLookupTable.SetTableValue(1, 1.0, 0, 0, 0.5)
        self.segmentationLabelImage.SetLookupTable(self.segmentationLabelLookupTable)
        self.segmentationLabelImage.UpdateWholeExtent()

        self.imageBlender = vtk.vtkImageBlend()
        self.imageBlender.AddInputData(self.imageMapToColors.GetOutput())
        self.imageBlender.AddInputData(self.segmentationLabelImage.GetOutput())
        self.imageBlender.SetOpacity(0, 1)
        self.imageBlender.SetOpacity(1, 1)
        self.imageBlender.UpdateWholeExtent()

        # self.commandSliceSelect = CommandSliceSelect()
        # self.commandSliceSelect.imageWindowLevel = self.imageWindowLevel
        # self.treePointLists.currentPoint = self.commandSliceSelect.currentPoint

        # self.commandSegment = CommandSegment()
        # self.commandSegment.setSegmentationImage(self.segmentationImage)
        # self.commandSegment.setRealImage(self.imageShiftScale.GetOutput())

        for i in range(3):
            self.vecReslice.append(vtk.vtkImageReslice())
            self.commandSliceSelect.vecImageReslice.append(self.vecReslice[i])
            self.commandSegment.vecImageReslice.append(self.vecReslice[i])

        self.vecReslice[0].SetResliceAxesDirectionCosines(1, 0, 0, 0, -1, 0, 0, 0, 1)
        self.vecReslice[1].SetResliceAxesDirectionCosines(0, 1, 0, 0, 0, 1, 1, 0, 0)
        self.vecReslice[2].SetResliceAxesDirectionCosines(1, 0, 0, 0, 0, 1, 0, 1, 0)

        for i in range(3):
            self.vecImageActor.append(vtk.vtkImageActor())

        for i in range(4):
            self.vecRenderer.append(vtk.vtkRenderer())
            self.commandSegment.vecRenderer.append(self.vecRenderer[i])

        self.treePointLists.ren = self.vecRenderer[3]
        self.treePointLists.image = self.imageWindowLevel.GetOutput()

        for i in range(3):
            # self.vecInteractorStyle.append(vtkInteractorStyleMy2D())
            self.vecInteractorStyle[i].InteractorNumber = i
            self.vecInteractorStyle[i].AddObserver(
                vtk.vtkCommand.UserEvent, self.commandSliceSelect
            )
            self.vecInteractorStyle[i].AddObserver(
                vtk.vtkCommand.WindowLevelEvent, self.commandSliceSelect
            )
            self.vecInteractorStyle[i].AddObserver(
                vtk.vtkCommand.StartWindowLevelEvent, self.commandSliceSelect
            )
            self.vecInteractorStyle[i].AddObserver(
                vtk.vtkCommand.SelectionChangedEvent, self.commandSliceSelect
            )
            # self.vecInteractorStyle[i].AddObserver(
            #     UserCommand.StartSegmentationAdd, self.commandSegment
            # )
            # self.vecInteractorStyle[i].AddObserver(
            #     UserCommand.StartSegmentationSub, self.commandSegment
            # )
            # self.vecInteractorStyle[i].AddObserver(
            #     UserCommand.StopSegmentationAdd, self.commandSegment
            # )
            # self.vecInteractorStyle[i].AddObserver(
            #     UserCommand.StopSegmentationSub, self.commandSegment
            # )
            # self.vecInteractorStyle[i].AddObserver(
            #     UserCommand.MoveSegmentationAdd, self.commandSegment
            # )
            # self.vecInteractorStyle[i].AddObserver(
            #     UserCommand.MoveSegmentationSub, self.commandSegment
            # )
            self.vecInteractorStyle[i].SegmentationModeEnabled = False
            self.segmentationList.vecInteractorStyle.append(self.vecInteractorStyle[i])

            self.commandSliceSelect.styleId[i] = self.vecInteractorStyle[i]
            self.commandSliceSelect.vecImageActor.append(self.vecImageActor[i])

            self.commandSegment.styleId[i] = self.vecInteractorStyle[i]

        for i in range(4):
            self.vecTextActor.append(vtk.vtkTextActor())
            self.vecTextActor[i].SetPosition(5, 5)
            self.vecRenderer[i].AddActor2D(self.vecTextActor[i])
            s = "L/W: %2.1f/%2.1f | (x,y,z): (%.1f, %.1f, %.1f)" % (
                50.0,
                100.0,
                0.0,
                0.0,
                0.0,
            )
            self.vecTextActor[i].SetInput(s)

        self.commandSliceSelect.vecTextActor = self.vecTextActor

        self.ui.qvtkWidget_ul.GetRenderWindow().AddRenderer(self.vecRenderer[0])
        self.ui.qvtkWidget_ur.GetRenderWindow().AddRenderer(self.vecRenderer[1])
        self.ui.qvtkWidget_ll.GetRenderWindow().AddRenderer(self.vecRenderer[2])
        self.ui.qvtkWidget_lr.GetRenderWindow().AddRenderer(self.vecRenderer[3])

        self.segmentationList.renderer = self.vecRenderer[3]
        self.segmentationList.segmentationBufferImage = self.segmentationImage
        self.segmentationList.commandSegment = self.commandSegment

        self.ui.qvtkWidget_ul.GetRenderWindow().GetInteractor().SetInteractorStyle(
            self.vecInteractorStyle[0]
        )
        self.ui.qvtkWidget_ur.GetRenderWindow().GetInteractor().SetInteractorStyle(
            self.vecInteractorStyle[1]
        )
        self.ui.qvtkWidget_ll.GetRenderWindow().GetInteractor().SetInteractorStyle(
            self.vecInteractorStyle[2]
        )
        self.commandSliceSelect.interactorStyleWindow3D = (
            self.ui.qvtkWidget_lr.GetRenderWindow().GetInteractor().GetInteractorStyle()
        )
        self.commandSegment.styleId[3] = (
            self.ui.qvtkWidget_lr.GetRenderWindow().GetInteractor().GetInteractorStyle()
        )

        for i in range(3):
            self.vecReslice[i].SetInputData(self.imageBlender.GetOutput())
            self.vecReslice[i].SetOutputDimensionality(2)
            self.vecReslice[i].SetInterpolationModeToLinear()
            self.vecReslice[i].UpdateWholeExtent()
            self.vecImageActorOrtho.append(vtk.vtkImageActor())
            self.vecImageActorOrtho[i].SetInputData(self.vecReslice[i].GetOutput())
            self.vecImageActorOrtho[i].SetUserMatrix(
                self.vecReslice[i].GetResliceAxes()
            )
            self.vecImageActor[i].SetInputData(self.vecReslice[i].GetOutput())
            self.vecRenderer[i].AddActor(self.vecImageActor[i])
            self.vecRenderer[3].AddActor(self.vecImageActorOrtho[i])

    def closeEvent(self, event):
        for i in range(4):
            self.vecRenderer[i].Delete()

        for i in range(3):
            self.vecReslice[i].Delete()

        for i in range(3):
            self.vecImageActor[i].Delete()

        self.imageReader.Delete()

    def on_actionExit_triggered(self):
        sys.exit()

    def on_actionOpen_triggered(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "c:\\temp", "Image Files (*.mhd)"
        )
        if not fileName:
            return

        self.ui.statusbar.showMessage("Reading file" + fileName)

        self.imageReader.SetFileName(fileName)
        self.imageReader.UpdateWholeExtent()
        image_range = self.imageReader.GetOutput().GetScalarRange()

        self.imageShiftScale.SetShift(-image_range[0])
        self.imageShiftScale.SetScale(255.0 / (image_range[1] - image_range[0]))
        self.imageShiftScale.UpdateWholeExtent()

        self.imageWindowLevel.SetWindow(100.0)
        self.imageWindowLevel.SetLevel(50.0)
        self.imageWindowLevel.UpdateWholeExtent()

        self.ui.qvtkWidget_ul.GetRenderWindow().Render()
        self.ui.qvtkWidget_ur.GetRenderWindow().Render()
        self.ui.qvtkWidget_ll.GetRenderWindow().Render()
        self.ui.qvtkWidget_lr.GetRenderWindow().Render()

    def on_buttonMaximize_ul_clicked(self):
        self.toggle_visibility(self.ui.qvtkWidget_ll)
        self.toggle_visibility(self.ui.qvtkWidget_ur)
        self.toggle_visibility(self.ui.qvtkWidget_lr)

    def on_buttonMaximize_ur_clicked(self):
        self.toggle_visibility(self.ui.qvtkWidget_ll)
        self.toggle_visibility(self.ui.qvtkWidget_ul)
        self.toggle_visibility(self.ui.qvtkWidget_lr)

    def on_buttonMaximize_ll_clicked(self):
        self.toggle_visibility(self.ui.qvtkWidget_ul)
        self.toggle_visibility(self.ui.qvtkWidget_ur)
        self.toggle_visibility(self.ui.qvtkWidget_lr)

    def on_buttonMaximize_lr_clicked(self):
        self.toggle_visibility(self.ui.qvtkWidget_ll)
        self.toggle_visibility(self.ui.qvtkWidget_ur)
        self.toggle_visibility(self.ui.qvtkWidget_ul)

    def toggle_visibility(self, widget):
        widget.setVisible(not widget.isVisible())

    def on_actionFullScreen_triggered(self, checked):
        if checked:
            self.showFullScreen()
        else:
            self.showNormal()
