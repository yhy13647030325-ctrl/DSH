# 官方快捷键定义（从手册 Reference 块提取）

> **来源**：《Blender 2.92 Manual》的 `Reference / Hotkey` 结构块。**每条都是官方原义**。

> **⚠ 同一键在不同编辑器/模式含义不同**——所以本表**按分区列出**，不要跨区套用。

> **写法差异**：本手册用 **`Ctrl-L`**（连字符），`blender-hard-surface` 用 **`Ctrl + L`**（加号）。**含义相同**。

> **鼠标缩写**：**LMB** 左键 / **RMB** 右键 / **MMB** 中键 / **Wheel** 滚轮 / **Numpad** 小键盘

## 建模（modeling，56 键）

| 快捷键 | 官方释义 |
|---|---|
| **Alt-C** | This toggles between an open curve and closed curve (Cyclic) |
| **Alt-D** | This tool takes any number of selected vertices and duplicate-drags them along the closest edge to th |
| **Alt-E** | Extrude edges as individual edges, use Alt-E to access the Extrude Edges |
| **Alt-F** | The Fill option will create triangular faces from any group of selected edges or vertices, as long as |
| **Alt-J** | This tool converts the selected triangles into quads by taking adjacent triangles and removing the sh |
| **Alt-L** | All selected normals are set to point from their vertex to the target after confirmed by Return or LM |
| **Alt-M** | Selection Y Splits (disconnects) the selection from the rest of the UV |
| **Alt-N** | There are a number of tools for editing custom split normals |
| **Alt-S** | The Radius allows you to directly control the width of the extrusion along the “spinal” curve |
| **Alt-T** | You can also reset the tilt to its default value (i |
| **Alt-V** | Rip fill works the same as the Rip tool above, but instead of leaving a hole, it fills in the gap wit |
| **Ctrl-A** | This tool is used to set a skin radius per vertex when using a Skin Modifier |
| **Ctrl-Alt-LMB** | In Edge select mode, holding Ctrl-Alt while selecting an edge (or two vertices) selects a sequence of |
| **Ctrl-B** | Menu Vertex ‣ Bevel Vertices (vertex bevel) Hotkey Shift-Ctrl-B (vertex bevel) The Bevel tool all |
| **Ctrl-H** | Hooks can be added to control one or more points with other objects |
| **Ctrl-L** | Select geometry connected to already selected elements |
| **Ctrl-LMB** | Selects the curve segments between two control points: the active and the one under the cursor |
| **Ctrl-M** | The Mirror tool is also available, behaving exactly as with mesh vertices |
| **Ctrl-NumpadPlus** | Menu Select ‣ Select More/Less ‣ Less Hotkey Ctrl-NumpadMinus With at least one vertex, edge, or |
| **Ctrl-P** | You can make other selected objects children of one or three control points, as with mesh objects |
| **Ctrl-R** | Loop Cut and Slide splits a loop of faces by inserting a new edge loop intersecting the chosen edge |
| **Ctrl-RMB** | Interactively places new points with Ctrl-RMB at the cursor position |
| **Ctrl-T** | This setting controls how the normals (visualized as arrows) twist around each control point – so it |
| **Ctrl-V** | The Minimize Stretch tool, reduces UV stretch by minimizing angles |
| **Ctrl-X** | This is a convenient shortcut that dissolves based on the current selection mode (vertex, edge, face) |
| **E** | Extrudes points by duplicating the selected points, which then can be moved, and connecting those poi |
| **E Extrude** | Faces duplicate faces, while keeping the new geometry connected with the original vertices |
| **F** | Connects two disconnected control points |
| **I** | This tool takes the currently selected faces and creates an inset of them, with adjustable thickness |
| **J** | This tool connects vertices in the order they are selected, splitting the faces between them |
| **K The** | Knife tool can be used to interactively subdivide (cut up) geometry by drawing lines or closed loops |
| **M** | This tool allows you to merge all selected vertices to a unique one, dissolving all others |
| **M At** | Center Moves selected UVs to their average position |
| **O Proportional** | Editing is available in UV editing |
| **P** | Curve objects that are made of multiple distinct curves can be separated into their own objects by se |
| **R N** | This is an interactive tool |
| **Shift-A** | See also When adding curves there are some common options like other Objects |
| **Shift-D** | This tool duplicates the selected control points, along with the curve segments implicitly selected ( |
| **Shift-E** | This edge property, a value between (0 |
| **Shift-G** | Selects control points that have certain similar properties to the active one |
| **Shift-N** | The Recalculate Handles operator rotates the selected control point’s handle to be tangential to the |
| **Shift-R** | This option works a bit like edge loop selection for meshes, inasmuch it selects a whole row of contr |
| **Shift-S** | Mesh snapping also works with curve components |
| **Shift-V** | Vertex Slide will transform a vertex along one of its adjacent edges |
| **Shift-W** | Bend Transform with Clamp on and off |
| **U** | Blender offers several ways of mapping UVs |
| **U Cube** | Projection maps the mesh onto the faces of a cube, which is then unfolded |
| **U Lightmap** | Pack takes each of a mesh’s faces, or selected faces, and packs them into the UV bounds |
| **U Reset** | UVs maps each face to fill the UV grid, giving each face the same mapping |
| **U Smart** | UV Project, cuts the mesh based on an angle threshold (angular changes in your mesh) |
| **U The** | Follow Active Quads tool takes the selected faces and lays them out by following continuous face loop |
| **V** | Handle types are a property of Bézier curves and can be used to alter features of the curve |
| **V The** | Stitch tool, will join selected UVs that share vertices |
| **X or** | Delete, Edge Loops Edge Loop allows you to delete a selected edge loop if it is between two other ed |
| **Y** | Splits (disconnects) the selection from the rest of the mesh |
| **Y The** | Split operator splits a selected segment of a curve from the rest of the curve |

## 界面（interface，19 键）

| 快捷键 | 官方释义 |
|---|---|
| **Alt-P** | To remove nodes from a frame, select and use Alt-P |
| **B** | To activate the tool, press B or click and drag LMB |
| **C Circle** | Select C allows you to select multiple items within a circular area |
| **Ctrl-Alt-Spacebar** | The fullscreen area contains only the main region of the editor |
| **Ctrl-G** | To create a node group, select the nodes you want to include, then press Ctrl-G, Group ‣ Make Group |
| **Ctrl-J** | Make a new frame including the selected nodes |
| **Ctrl-P** | Once a frame node is placed, nodes can be added by dropping them onto the frame or by selecting the n |
| **Ctrl-RMB** | Lasso Select is used to create a free-form selection |
| **Ctrl-Spacebar** | The maximized area fill the whole application window |
| **Ctrl-Z** | If you want to undo your last action, just press Ctrl-Z |
| **F3 The** | Menu Search pop-up searches Blender’s interface for a desired tool and allows you to execute that too |
| **F9** | After an operation is complete you can tweak the parameters of the operation afterwards |
| **LMB** | Clicking on an item selects it, using modifier keys you can perform other operations |
| **M** | Muting a node removes the contribution of the node to the node tree, and makes all links pass through |
| **Q The** | Quick Favorites menu gather your favorite tools |
| **Shift-A** | Nodes are added via the Add menu or using the Shift-A shortcut |
| **Shift-D** | Click LMB or RMB on the desired node, press Shift-D and move the mouse away to see the duplicate of t |
| **Shift-R** | The Repeat Last feature will repeat your last action when you press Shift-R |
| **Shift-Spacebar** | You can switch tools with a toolbar that will pop up at the location of your cursor after pressing Sh |

## 场景与物体（scene_layout，22 键）

| 快捷键 | 官方释义 |
|---|---|
| **A** | Select all selectable objects |
| **Alt-A** | Deselect all objects, but the active object stays the same |
| **Alt-D** | You also have the choice of creating a Linked Duplicate rather than a Duplicate; this is called a dee |
| **Alt-P** | You can remove a parent-child relationship via Alt-P |
| **B** | Interactive box selection |
| **C** | Interactive circle selection |
| **Ctrl-A** | Applying transform values essentially resets the values of object’s location, rotation or scale, whil |
| **Ctrl-I** | Toggle the selection state of all visible objects |
| **Ctrl-J** | Join merges all selected objects into the last selected Active object |
| **Ctrl-L** | Links objects between scenes or data-blocks of the active object to all selected objects |
| **Ctrl-M** | Mirroring an object or mesh selection will create a reversed version of the selection |
| **Ctrl-P** | To parent objects, select at least two objects (select the child objects first, and select the parent |
| **G In** | Object Mode, the move option lets you move objects |
| **R** | Rotation is also known as a spin, twist, orbit, pivot, revolve, or roll and involves changing the ori |
| **R R** | A free rotation mode |
| **S** | Scaling means changing proportions of objects |
| **Shift-A** | New objects can be created with the Add menu in the 3D Viewport’s header |
| **Shift-D** | This will create a visually-identical copy of the selected object(s) |
| **Shift-G** | There are two ways to organize the objects in relation to one another |
| **Shift-L** | Selects all objects which share a common data-block with the active object |
| **Shift-S** | The Snap menu (also available from the 3D header in both Object Mode and Edit Mode Object ‣ Snap and |
| **X or** | Delete Delete the selected objects from the current scene |

## 动画与绑定（animation，32 键）

| 快捷键 | 官方释义 |
|---|---|
| **Alt-E** | Relax pose is somewhat related to the above topic, but it is only useful with keyframed bones |
| **Alt-F** | This tool allows you to switch the direction of the selected bones (i |
| **Alt-I** | There are several methods of removing keyframes: - In the 3D Viewport press Alt-I to remove keys fr |
| **Alt-L** | Interactively browse poses in the 3D Viewport |
| **Alt-P** | The Propagate tool copies the pose of the selected bones on the current frame over to the keyframes d |
| **Alt-S** | You can alter the radius that a bone has by selecting the head, body or tail of a bone, and then pres |
| **Ctrl-A** | Pose as Rest Pose Conversely, you may define the current pose as the new rest pose (i |
| **Ctrl-B** | Bind Camera to Markers is a special operator only available in the Timeline |
| **Ctrl-D** | The usual way to add a driver to a property is to RMB click a property, then choose Add Driver in the |
| **Ctrl-E** | Push Pose interpolates the current pose by making it closer to the next keyframed position |
| **Ctrl-L** | Selects all the bones in the chain which the active (last selected) bone belongs to |
| **Ctrl-M** | Having dozens of markers scattered throughout your scene’s time will not help you much unless you kno |
| **Ctrl-N** | Axis Orientation Local Tangent Align roll relative to the axis defined by the bone and its parent |
| **Ctrl-P** | Armature Deform Parenting is a way of creating and setting up an Armature Modifier |
| **Ctrl-R** | This is a transform mode where you can edit the roll of all selected bones |
| **Ctrl-RMB** | If at least one bone is selected, Ctrl-RMB-clicking adds a new bone |
| **F** | The main use of this tool is to create one bone between two selected joints by pressing F, similar to |
| **G** | Once you have one or more markers selected, press G, while hovering with the mouse over the marker ba |
| **I** | There are several methods of adding new keys |
| **K** | Some ways to add properties to keying sets |
| **L** | Selects all the bones in the chain which the active (last selected) bone belongs to |
| **LMB** | Click LMB on the marker’s triangle to select it |
| **LMB-drag** | Creates a suitable breakdown pose on the current frame |
| **M** | The simplest way to add a marker is to move to the frame where you would like it to appear, and press |
| **N Reference** | Menu Context menu ‣ Edit Driver Hotkey Ctrl-D This panel is visible in Sidebar of the Drivers Edi |
| **P** | You can, as with meshes, separate the selected bones in a new armature object Armature ‣ Separate, Ct |
| **Shift-A** | In the 3D Viewport, Shift-A to add a new bone to your armature |
| **Shift-D** | You can duplicate the selected markers by pressing Shift-D |
| **Shift-G** | Children Extends the selection to all hierarchical descendant bones |
| **Shift-L** | If a pose is added, a pose marker is created |
| **X** | To delete the selected markers simply press X, and confirm the pop-up message with LMB |
| **Y** | Disconnects the selection and clears the parent at the start and end |

## 雕刻与绘制（sculpt_paint，18 键）

| 快捷键 | 官方释义 |
|---|---|
| **Alt-M** | Fills the mask with a value of 0 |
| **B** | Works like the Box Select tool, it creates a rectangular mask region |
| **C** | Similar to the Draw brush, but includes settings to adjust the plane on which the brush acts |
| **Ctrl-D** | Dynamic topology (aka dyntopo) is a dynamic tessellation sculpting method, adds and removes details o |
| **Ctrl-I** | Inverts an existing mask |
| **G** | Used to drag a group of vertices around |
| **I** | Similar to Draw, except that vertices in Inflate mode are displaced in the direction of their own nor |
| **K** | Pulls vertices along with the movement of the brush to create long, snake-like forms |
| **L** | This brush is similar to Draw, except that the height of the displacement layer is capped |
| **M** | Lets you select mesh parts to be unaffected by other brushes by painting vertex colors |
| **P** | Pulls vertices towards the center of the brush |
| **S** | Eliminates irregularities in the area of the mesh within the brush’s influence by smoothing the posit |
| **Shift-A** | Creates a mask radiating outwards from the active vertex in a uniform manner |
| **Shift-C** | Creates sharp indents or ridges by pushing or pulling the mesh, while pinching the vertices together |
| **Shift-Ctrl-LMB** | Can be used to create a free-form mask, similar to the Lasso Select tool |
| **Shift-T** | The Flatten brush determines an “area plane” located by default at the average height above/below the |
| **V** | In this mode you can select one or more vertices and then paint only on the selection |
| **X** | Moves vertices inward or outward, based the average normal of the vertices contained within the drawn |

## 编辑器（editors，30 键）

| 快捷键 | 官方释义 |
|---|---|
| **Alt-B** | Allows you to define a clipping region to limit the 3D Viewport display to a portion of 3D space |
| **Alt-C** | Baking a curve replaces it with a set of sampled points, and removes the ability to edit the curve |
| **Alt-D** | The contents of one Action strip can be instanced multiple times |
| **Alt-O** | There is also an option to smooth the selected curves, but beware: its algorithm seems to be to divid |
| **Alt-Period** | The active element can be an object, vertex, edge or a face |
| **Comma Transform** | Orientations affect the behavior of Transformations |
| **Ctrl-E** | Sets the easing mode of the selected keyframes |
| **Ctrl-G** | Places the 2D cursor at the center of the selected keyframes |
| **Ctrl-LMB** | Selects all UV components along the shortest path from the active component to the one which was sele |
| **Ctrl-M** | Selected keyframes can be mirrored over different properties using the Mirror Keys tool |
| **Home** | Centers the camera view inside the 3D Viewport’s screen area and resizes the view to fit within the a |
| **M** | Objects can be removed from Local View by selecting them and using the Remove from Local View operato |
| **Numpad0** | This switches the view to the active camera |
| **Numpad5** | This operator changes the projection of the viewport camera |
| **Period** | The 3D cursor is the most intuitive of the pivot points |
| **Period The** | Median Point can be considered to be broadly similar to the concept of Center of Gravity (COG) |
| **Shift-AccentGrave** | Menu View ‣ Navigation ‣ Walk Navigation On activation the mouse pointer will move at the center of |
| **Shift-B** | The Zoom Region tool allows you to specify a rectangular region and zoom in so that the region fills |
| **Shift-Ctrl-MMB** | In most cases its sufficient to zoom the view to get a closer look at something, however, you may not |
| **Shift-Ctrl-Tab** | Snap target options become active when either Vertex, Edge, Face, or Volume is selected as the snap e |
| **Shift-D** | Duplicates the selected keyframes |
| **Shift-E** | Extrapolation defines the behavior of a curve before the first and after the last keyframes |
| **Shift-S** | Keyframes can be snapped to different properties by using the Snap Keys tool |
| **Shift-Tab** | The ability to snap objects and mesh element to various types of scene elements during a transformati |
| **T** | Sets the interpolation mode between the selected keyframes |
| **Tab** | The contents of Action strips can be edited, but you must be in Tweak Mode to do so |
| **U** | This tool ensures that none of the selected strips use an action which is also used by any other stri |
| **V** | Sets the handle type of the selected keyframes |
| **X** | Acts like the Clean Keyframes tool but will also delete the channel itself if it is only left with a |
| **X Clean** | Keyframes resets the keyframe tangents on selected keyframes to their auto-clamped shape, if they hav |

## 蜡笔（grease_pencil，19 键）

| 快捷键 | 官方释义 |
|---|---|
| **Ctrl-C** | Copy the selected points/strokes to the clipboard |
| **Ctrl-E** | Interpolates strokes between the previous and next keyframe by adding a single keyframe |
| **Ctrl-M** | The Mirror tool is also available, behaving exactly the same as with mesh vertices |
| **Ctrl-V** | Type Paste to Active Pastes the points/strokes copied from the clipboard into the active layer |
| **E** | Extrudes points by duplicating the selected points, which then can be moved |
| **F** | Close or open strokes by connecting the last and first point |
| **I** | The stroke animation tools are described in the Animation section |
| **M** | A pop-up menu to move the stroke to a different layer |
| **P** | Separate the selected elements into a new Grease Pencil object |
| **Shift-A** | In Object Mode, the Add Grease Pencil menu provides three different Grease Pencil primitives: [IMG] |
| **Shift-D** | Duplicates the selected elements, without creating any connections with the rest of the strokes (unli |
| **Shift-G** | Layer Selects all the points/strokes on the same layer |
| **Shift-I** | Active Layer Add a new blank keyframe to the active layer at the current frame |
| **Shift-L** | Selects alternate points in the selected strokes |
| **Shift-S** | Mesh snapping also works with Grease Pencil components |
| **Shift-X** | Deletes the last keyframe in the Dope Sheet or the current keyframe if you are on one |
| **U Grease** | Pencil materials can be created in the Material properties as any other materials in Blender |
| **V** | Splits (disconnects) the selected points from the rest of the stroke |
| **Y** | Select the active layer |

## 视频编辑（video_editing，13 键）

| 快捷键 | 官方释义 |
|---|---|
| **Alt-O** | To reset the (soft) start/end frame handles |
| **Alt-S** | Swaps the first two inputs for the effect strip |
| **Backspace** | Remove blank frames between the current frame and the first strip to the left, independent of selecti |
| **E** | With a number of strips selected, pressing E lets you interactively extend the strips |
| **Equals** | Insert blank frames between the current frame and the first strips to the right, independent of selec |
| **G Pressing** | G moves all the selected strip(s) |
| **K** | This splits the selected strip in two at the current frame |
| **R** | This tool can be used to assign (reconnect) effect strips in a different way |
| **S The** | Slip tool allows you to change the position of the contents of a strip without moving the strip itsel |
| **Shift-D** | Duplicate a strip to make an unlinked copy; drag it to a time and channel, and drop it by LMB click |
| **Shift-K** | Like Split, it splits a strip in two distinct strips; however you will not be able to drag the endpoi |
| **Shift-S** | Moves the strip or control point to the current frame |
| **Y** | For images sequence only – Converts the strip into multiple strips, one strip for each frame |

## 追踪（movie_clip，18 键）

| 快捷键 | 官方释义 |
|---|---|
| **A** | Selects all items |
| **Alt-C** | Toggle to create a closed curve or open it again |
| **Alt-Left** | Tracks the motion backward by one frame |
| **Alt-O** | Force reload the currently loaded movie clip |
| **Alt-Right** | Tracks the motion forward one frame |
| **Alt-T** | Deletes all tracked and keyframed markers before the current frame for all selected tracks |
| **B** | See Box Select |
| **C See** | Circle Select |
| **Ctrl-I** | Selects non-selected items and deselects existing selection |
| **Ctrl-J** | This operator joins all selected tracks into one |
| **Ctrl-N** | Make normals (handle directions) consistent |
| **Ctrl-T** | Tracks the motion forward along the whole sequence |
| **P** | Fills cache with frames |
| **Shift-A** | There are two primitives available: a Bézier Circle and a Square with vector handles |
| **Shift-G** | Select all tracks from specified group |
| **Shift-T** | Deletes all tracked and keyframed markers after the current frame for all selected tracks |
| **V** | Set handle type for selected spline points |
| **X** | Removes control points |

## 插件（addons，14 键）

| 快捷键 | 官方释义 |
|---|---|
| **Alt-L** | Clear labels of selected nodes |
| **Alt-R** | All of the images used in the node tree (Image inputs, textures) can be reloaded by hitting Alt-R |
| **Alt-S** | Select two nodes that have something linked to their outputs |
| **Alt-X** | Clean your node tree |
| **Ctrl-NumpadPeriod** | Z-Combine nodes will be used for merging |
| **Ctrl-T** | Select any shader node, Ctrl-T and an image texture with nodes controlling coordinates will be added |
| **O** | In compositing – link to Composite output |
| **Shift-A** | Rigify stores all the information required to generate complex rig controls and mechanism in more sim |
| **Shift-C** | Copy settings of active node to all selected nodes of the same type |
| **Shift-Ctrl-LMB** | Viewer Node for shaders |
| **Shift-P** | Select nodes and “wrap” them in Frame node by hitting Shift-P |
| **Shift-S** | Change the type of selected node(s) to any other type |
| **Slash** | Reroute nodes will be added and linked to each output of each selected node |
| **Z** | Reset position and scale of the backdrop |

## 文件（files，4 键）

| 快捷键 | 官方释义 |
|---|---|
| **Ctrl-F2** | The Batch Rename operator can rename many data-block names at once |
| **Ctrl-O** | The upper text field displays the current directory path, and the lower text field contains the selec |
| **Ctrl-S** | Reference Menu File ‣ Save As… Hotkey Shift-Ctrl-S Reference Menu File ‣ Save Copy… There are |
| **F2 The** | Rename Active Item operator renames the active Bone, Node, Object and Sequence Strip |

## 入门（getting_started，1 键）

| 快捷键 | 官方释义 |
|---|---|
| **Alt-F1** | You may want to access help for a tool or area from within Blender |

---

## 两本技能的键位写法对照（示例）

| 含义 | 本手册（官方） | blender-hard-surface（项目书） |
|---|---|---|
| 环切 | `Ctrl-R` | `Ctrl + R` |
| 倒角 | `Ctrl-B` | `Ctrl + B` |
| 沿法线缩放 | `Alt-S` | `Alt + S` |
| 选松散部件 | `L` | `L` |
| 复制 | `Shift-D` | `Shift + D` |
| Snap 菜单 | `Shift-S` | `Shift + S` |
| 重算法线 | `Shift-N`（2.92 时代） | `Ctrl + N`（书中标注新版） |

> **⚠ 重要版本差异**：**2.92 手册写的是 `Shift-N`（Recalculate Normals Outside）**，
> 而 `blender-hard-surface` 明确写「**Ctrl + N（新版），Shift + N（旧版）**」。
> **现在（3.x/4.x）用 `Ctrl-N`。** 本技能保留手册原写法，但在此标注。

## 高频键 Top 25（按全书出现次数）

| 快捷键 | 次数 | 说明 |
|---|---|---|
| `Shift-LMB` | 106 | 加选/多选 |
| `Ctrl-LMB` | 89 | 特殊选择（各上下文不同） |
| `Ctrl-RMB` | 61 | 套索选择（Lasso） |
| `Alt-LMB` | 52 | 边循环选择（Select Loop） |
| `Ctrl-P` | 34 | 父级设置（依上下文：物体/骨骼/节点） |
| `Alt-A` | 23 | 取消全选 |
| `Alt-S` | 22 | 沿法线缩放（网格）/ 改骨骼半径（骨骼） |
| `Ctrl-MMB` | 21 | 缩放视图 |
| `Ctrl-C` | 21 | 复制 |
| `Ctrl-L` | 21 | 关联数据/全选相连 |
| `Alt-Backspace` | 21 | 删除/输入特殊字符 |
| `Ctrl-A` | 19 | 应用（缩放/旋转/位置） |
| `Shift-A` | 19 | 添加菜单（Add） |
| `Shift-D` | 19 | 复制 |
| `Ctrl-I` | 18 | 反选 |
| `Shift-G` | 17 | 选择相似 |
| `Shift-RMB` | 16 | 上下文菜单 |
| `Alt-P` | 16 | 清空父级/断开 |
| `Shift-F` | 16 | 填充/进入某模式 |
| `Shift-S` | 14 | Snap 吸附菜单 |
| `Ctrl-Tab` | 14 | 切换物体类型模式 |
| `Ctrl-X` | 14 | 剪切 |
| `Ctrl-V` | 14 | 粘贴 |
| `Ctrl-G` | 14 | 编组/合并 |
| `Shift-Ctrl-LMB` | 13 |  |
