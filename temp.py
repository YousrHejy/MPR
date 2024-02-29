# """
# =========================================================================

#   Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
#   All rights reserved.
#   See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

#      This software is distributed WITHOUT ANY WARRANTY; without even
#      the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#      PURPOSE.  See the above copyright notice for more information.

# =========================================================================*/

# """

# First access the VTK module (and any other needed modules) by importing them.
# noinspection PyUnresolvedReferences

# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderer,
    vtkRenderWindowInteractor,
)


def main(argv):
    colors = vtkNamedColors()

    #
    # Next we create an instance of vtkConeSource and set some of its
    # properties. The instance of vtkConeSource 'cone' is part of a
    # visualization pipeline (it is a source process object) it produces data
    # (output type is vtkPolyData) which other filters may process.
    #
    cone = vtkConeSource()
    cone.SetHeight(2.0)
    cone.SetRadius(1.0)
    cone.SetResolution(10)

    #
    # In this example we terminate the pipeline with a mapper process object.
    # (Intermediate filters such as vtkShrinkPolyData could be inserted in
    # between the source and the mapper.)  We create an instance of
    # vtkPolyDataMapper to map the polygonal data into graphics primitives. We
    # connect the output of the cone source to the input of this mapper.
    #
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())

    #
    # Create an actor to represent the cone. The actor orchestrates rendering
    # of the mapper's graphics primitives. An actor also refers to properties
    # via a vtkProperty instance, and includes an internal transformation
    # matrix. We set this actor's mapper to be coneMapper which we created
    # above.
    #
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(colors.GetColor3d("Yellow"))

    #
    # Create two renderers and assign actors to them. A renderer renders into
    # a viewport within the vtkRenderWindow. It is part or all of a window on
    # the screen and it is responsible for drawing the actors it has.  We also
    # set the background color here. In this example we are adding the same
    # actor to two different renderers it is okay to add different actors to
    # different renderers as well.
    #

    renderers = []
    for i in range(4):
        ren = vtkRenderer()
        ren.AddActor(coneActor)
        renderers.append(ren)

    renderers[0].SetBackground(colors.GetColor3d("Green"))
    renderers[0].SetViewport(
        0.0, 0.5, 0.5, 1
    )  # (xmin, ymin, xmax, ymax) from left down

    renderers[1].SetBackground(colors.GetColor3d("DodgerBlue"))
    renderers[1].SetViewport(0.5, 0.5, 1.0, 1.0)

    renderers[2].SetViewport(0.0, 0.0, 0.5, 0.5)

    renderers[3].SetBackground(colors.GetColor3d("Red"))
    renderers[3].SetViewport(0.5, 0, 1.0, 0.5)

    # Finally we create the render window which will show up on the screen.
    # We put our renderer into the render window using AddRenderer. We also
    # set the size to be 300 pixels by 300.

    renWin = vtkRenderWindow()
    for ren in renderers:
        renWin.AddRenderer(ren)
    renWin.SetSize(800, 800)
    renWin.SetWindowName("Tutorial_Step3")

    # Render
    renWin.Render()

    # The vtkRenderWindowInteractor class watches for events (e.g., keypress,
    # mouse) in the vtkRenderWindow. These events are translated into
    # event invocations that VTK understands (see VTK/Common/vtkCommand.h
    # for all events that VTK processes). Then observers of these VTK
    # events can process them as appropriate.
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    #
    # By default the vtkRenderWindowInteractor instantiates an instance
    # of vtkInteractorStyle. vtkInteractorStyle translates a set of events
    # it observes into operations on the camera, actors, and/or properties
    # in the vtkRenderWindow associated with the vtkRenderWinodwInteractor.
    # Here we specify a particular interactor style.
    style = vtkInteractorStyleTrackballCamera()
    iren.SetInteractorStyle(style)

    #
    # Unlike the previous scripts where we performed some operations and then
    # exited, here we leave an event loop running. The user can use the mouse
    # and keyboard to perform the operations on the scene according to the
    # current interaction style. When the user presses the 'e' key, by default
    # an ExitEvent is invoked by the vtkRenderWindowInteractor which is caught
    # and drops out of the event loop (triggered by the Start() method that
    # follows.
    #
    iren.Initialize()
    iren.Start()

    #
    # Final note: recall that observers can watch for particular events and
    # take appropriate action. Pressing 'u' in the render window causes the
    # vtkRenderWindowInteractor to invoke a UserEvent. This can be caught to
    # popup a GUI, etc. See the Tcl Cone5.tcl example for an idea of how this
    # works.


if __name__ == "__main__":
    import sys

    main(sys.argv)


# import vtk


# class CustomInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):
#     def __init__(self):
#         self.AddObserver("LeftButtonPressEvent", self.left_button_press_event)

#     def left_button_press_event(self, obj, event):
#         # Override the default behavior on left button press
#         return


# def main():
#     colors = vtk.vtkNamedColors()

#     # Load image
#     reader = vtk.vtkMetaImageReader()
#     reader.SetFileName("out.mhd")
#     reader.Update()

#     # Create renderers
#     renderer_left = vtk.vtkRenderer()
#     renderer_left.SetViewport(0.0, 0.0, 1.0, 1.0)  # Left half of the render window
#     renderer_left.SetBackground(colors.GetColor3d("NavajoWhite"))

#     # Setup render window.
#     render_window = vtk.vtkRenderWindow()
#     render_window.SetSize(1200, 600)  # Double width to accommodate two renderers
#     render_window.AddRenderer(renderer_left)
#     render_window.SetWindowName("Image Slicing")

#     renderer_left.ResetCamera()

#     # Setup render window interactor.
#     render_window_interactor = vtk.vtkRenderWindowInteractor()
#     render_window_interactor.SetRenderWindow(render_window)

#     # Set the custom interactor style
#     custom_interactor_style = CustomInteractorStyle()
#     render_window_interactor.SetInteractorStyle(custom_interactor_style)

#     # Create cutting plane widget
#     cutting_plane_widget = vtk.vtkImagePlaneWidget()
#     cutting_plane_widget.SetInputConnection(reader.GetOutputPort())
#     cutting_plane_widget.SetInteractor(render_window_interactor)
#     cutting_plane_widget.DisplayTextOn()
#     cutting_plane_widget.SetPlaneOrientationToZAxes()  # Initial orientation to Z axes
#     cutting_plane_widget.On()

#     # Initialize variables for dragging
#     start_position = None

#     def drag_cutting_plane(widget, event):
#         nonlocal start_position

#         if start_position is not None:
#             # Get current cursor position
#             current_position = render_window_interactor.GetEventPosition()

#             # Calculate the displacement
#             displacement = [current_position[i] - start_position[i] for i in range(2)]

#             # Move the cutting plane
#             cutting_plane_widget.GetPlaneProperty().AddObserver(
#                 vtk.vtkCommand.ModifiedEvent, update_cutting_plane
#             )
#             cutting_plane_widget.UpdatePlacement()
#             cutting_plane_widget.GetPlaneProperty().RemoveObservers(
#                 vtk.vtkCommand.ModifiedEvent
#             )

#             # Update the start position for the next event
#             start_position = current_position

#             # Update the render window
#             render_window.Render()

#     def stop_dragging(widget, event):
#         nonlocal start_position
#         if event == "LeftButtonReleaseEvent":
#             start_position = None

#     def update_cutting_plane(obj, event):
#         cutting_plane_widget.UpdatePlacement()

#     # Add observers for dragging events
#     render_window_interactor.AddObserver(
#         vtk.vtkCommand.LeftButtonPressEvent, start_dragging
#     )
#     render_window_interactor.AddObserver(
#         vtk.vtkCommand.MouseMoveEvent, drag_cutting_plane
#     )
#     render_window_interactor.AddObserver(
#         vtk.vtkCommand.LeftButtonReleaseEvent, stop_dragging
#     )

#     # Create image slice actor and mapper for the original image
#     image_slice_mapper_left = vtk.vtkOpenGLImageSliceMapper()
#     image_slice_mapper_left.SetInputConnection(reader.GetOutputPort())
#     image_slice_mapper_left.SliceAtFocalPointOn()  # Set slice orientation at focal point

#     image_slice_actor_left = vtk.vtkImageSlice()
#     image_slice_actor_left.SetMapper(image_slice_mapper_left)

#     # Add the image slice actor to the left renderer
#     renderer_left.AddActor(image_slice_actor_left)

#     # Set the opacity of the original image to 0 in the right renderer
#     image_slice_actor_left.GetProperty().SetOpacity(0)

#     # Render and start interaction.
#     render_window.Render()
#     render_window_interactor.Start()


# if __name__ == "__main__":
#     main()
