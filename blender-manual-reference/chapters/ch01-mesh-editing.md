# 第 1 章：网格编辑工具（官方 Reference）

> 出自《Blender 2.92 Manual》建模区（619,233 字符 / 290 页）。
> **本章按官方 Reference 块整理：Mode / Menu / Hotkey 三者齐全**——这是手册最可靠的部分。

> **快捷键写法**：官方用 `Ctrl-R`（连字符）。`blender-hard-surface` 用 `Ctrl + R`，含义相同。

---

## 1.1 官方工具清单（含 Menu 与 Hotkey）

| 工具 | 快捷键 | 菜单路径 |
|---|---|---|
| **Primitives** | `Shift-A` | Add ‣ Curve |
| **Select Random** | `L, Ctrl-L, Shift-L` | Select ‣ Select Random |
| **Extrude Curve and Move** | `E` | Curve ‣ Extrude Curve and Move |
| **Transform** | `Alt-S` | Curve ‣ Transform |
| **Set Goal Weight** | `Ctrl-RMB` | Context Menu ‣ Set Goal Weight |
| **Primitives** | `Shift-A` | Add ‣ Mesh |
| **Properties** | `Alt-N` | Mesh ‣ Normals ‣ Split |
| **UV Tools** | `U` | Header ‣ UV |
| **Bevel Edges** | `Ctrl-B` | Edge ‣ Bevel Edges |
| **Edge Crease** | `Shift-E` | Edge ‣ Edge Crease |
| **Extrude Edges** | `Alt-E` | Edge ‣ Extrude Edges |
| **Loop Cut and Slide** | `Ctrl-R` | Edge ‣ Loop Cut and Slide |
| **Offset Edge Slide** | `Shift-Ctrl-R` | — |
| **Extrude Faces** | `E` | Mesh ‣ Face ‣ Extrude Faces |
| **Extrude Faces Along Normals** | `Alt-E` | Mesh ‣ Extrude ‣ Extrude Faces Along Normals |
| **Extrude Individual Faces** | `Alt-E` | Mesh ‣ Extrude ‣ Individual Faces |
| **Fill** | `Alt-F` | Face ‣ Fill |
| **Inset Faces** | `I` | Face ‣ Inset Faces |
| **Triangles to Quads** | `Alt-J` | Face ‣ Triangles to Quads |
| **Triangulate Faces** | `Ctrl-T` | Face ‣ Triangulate Faces |
| **Deleting & Dissolving** | `X, Delete` | Mesh ‣ Delete |
| **Duplicate** | `Shift-D` | Mesh ‣ Duplicate |
| **Extrude** | `Alt-E` | Mesh ‣ Extrude |
| **Merge** | `M` | Mesh ‣ Merge, |
| **Mirror** | `Ctrl-M` | Mesh ‣ Mirror |
| **Flip** | `Ctrl-N and Shift-Ctrl-N` | Mesh ‣ Normals ‣ Flip |
| **Separate** | `P` | Mesh ‣ Separate |
| **Split** | `Alt-M` | Mesh ‣ Split |
| **Bend** | `Shift-W` | Object/Mesh/Curve/Surface ‣ Transform ‣ Bend |
| **Shear** | `Shift-Ctrl-Alt-S` | Object/Mesh/Curve/Surface ‣ Transform ‣ Shear |
| **Shrink Fatten** | `Alt-S` | Mesh ‣ Transform ‣ Shrink Fatten |
| **Skin Resize** | `Ctrl-A` | Mesh ‣ Transform ‣ Skin Resize |
| **To Sphere** | `Shift-Alt-S` | Mesh ‣ Transform ‣ To Sphere |
| **Bevel Vertices** | `Shift-Ctrl-B` | Vertex ‣ Bevel Vertices |
| **Connect Vertex Path** | `J` | Vertex ‣ Connect Vertex Path |
| **Extrude Vertices** | `Alt-E` | Vertex ‣ Extrude Vertices |
| **Hooks** | `Ctrl-H` | Vertex ‣ Hooks |
| **New Edge/Face from Vertices** | `F` | Vertex ‣ New Edge/Face from Vertices |
| **Make Vertex Parent** | `Ctrl-P` | Vertex ‣ Make Vertex Parent |
| **Rip Vertices** | `V` | Vertex ‣ Rip Vertices |
| **Rip Vertices and Extend** | `Alt-D` | Vertex ‣ Rip Vertices and Extend |
| **Rip Vertices and Fill** | `Alt-V` | Vertex ‣ Rip Vertices and Fill |
| **Slide Vertices** | `Shift-V` | Vertex ‣ Slide Vertices |
| **Vertex Groups Panel** | `Ctrl-G` | Vertex ‣ Vertex Groups |
| **Selection Modes** | `1, 2, 3` | 3D Viewport Header ‣ Select Mode |
| **Linked** | `Ctrl-L` | Select ‣ Select Linked ‣ Linked |
| **Edge Loops** | `Alt-LMB, or Shift-Alt-LMB for modifying existing selection.` | Select ‣ Select Loops ‣ Edge Loops |
| **Mirror Selection** | `Shift-Ctrl-M` | Select ‣ Mirror Selection |
| **Select More/Less** | `Ctrl-NumpadPlus` | Select ‣ Select More/Less ‣ More |
| **Select Similar** | `Shift-G` | Select ‣ Similar |
| **Extrude to Cursor** | `Ctrl-RMB` | — |
| **Extrude Manifold** | `Alt-E` | Mesh ‣ Extrude ‣ Extrude Manifold |
| **Extrude Region** | `E` | — |
| **Knife** | `K` | — |
| **Loop Cut** | `Ctrl-R` | — |
| **Transform** | `Ctrl-M` | UV ‣ Transform |
| **Rip** | `V` | — |
| **Active Element** | `X, Delete` | — |
| **Primitives** | `Shift-A` | Add ‣ Metaball |
| **Primitives** | `Shift-A` | Add ‣ Curve |
| **Select Random** | `L, Ctrl-L` | Select ‣ Select Random |
| **Extrude Curve and Move** | `E` | Surface ‣ Extrude Curve and Move |
| **Transform** | `Ctrl-M` | Surface ‣ Transform |

---

## 1.2 无快捷键但重要的工具（只能走菜单）

| 工具 | 菜单路径 |
|---|---|
| **Subdivide** | Curve ‣ Segments ‣ Subdivide |
| **Active Spline** | Properties ‣ Curve ‣ Active Spline |
| **Bridge Edge Loops** | Edge ‣ Bridge Edge Loops |
| **Edge Slide** | Edge ‣ Edge Slide |
| **Rotate Edge** | Edge ‣ Rotate Edge CW / Rotate Edge CCW |
| **Screw** | Edge ‣ Screw |
| **Subdivide** | Edge ‣ Subdivide |
| **Un-Subdivide** | Edge ‣ Un-Subdivide |
| **Beautify Faces** | Face ‣ Beautify Faces |
| **Grid Fill** | Face ‣ Grid Fill |
| **Poke Faces** | Faces ‣ Poke Faces |
| **Shade Smooth** | Face ‣ Shade Smooth |
| **Solidify Faces** | Face ‣ Solidify Faces |
| **Weld Edges into Faces** | Face ‣ Weld Edges into Faces |
| **Wireframe** | Face ‣ Wireframe |
| **Bisect** | Mesh ‣ Bisect |
| **Decimate Geometry** | Mesh ‣ Clean up ‣ Decimate Geometry |
| **Convex Hull** | Mesh ‣ Convex Hull |
| **Knife Project** | Mesh ‣ Knife Project |
| **Shading** | Mesh ‣ Shading |
| **Snap to Symmetry** | Mesh ‣ Snap to Symmetry |
| **Sort Elements** | Mesh ‣ Sort Elements… |
| **Symmetrize** | Mesh ‣ Symmetrize |
| **Push/Pull** | Object/Mesh ‣ Transform ‣ Push/Pull |
| **Randomize** | Mesh ‣ Transform ‣ Randomize |
| **Warp** | Object/Mesh/Curve/Surface ‣ Transform ‣ Warp |
| **Blend from Shape** | Vertex ‣ Blend from Shape |
| **Connect Vertex Pairs** | Vertex ‣ Connect Vertex Pairs |
| **Laplacian Smooth** | Context Menu ‣ Laplacian Smooth |
| **Propagate to Shapes** | Vertex ‣ Propagate to Shapes |
| **Smooth Vertices** | Vertex ‣ Smooth Vertices, |
| **Non-Manifold** | Select ‣ Select All by Trait ‣ Non-Manifold |
| **Checker Deselect** | Select ‣ Checker Deselect |
| **Select Random** | Select ‣ Select Random |
| **Select Sharp Edges** | Select ‣ Select Sharp Edges |
| **Side of Active** | Select ‣ Side of Active |
| **Options** | Sidebar ‣ Tool ‣ Options ‣ Auto Merge |
| **Texture Space** | Object ‣ Transform ‣ Scale/Move Texture Space |
| **Mark Seam** | Edge ‣ Mark/Clear Seam |
| **Subdivide** | Surface ‣ Segments ‣ Subdivide |
| **Active Spline** | Properties ‣ Curve ‣ Active Spline |
| **Text** | 3D Viewport ‣ Text |
| **Introduction** | Add ‣ Text |

---

## 1.3 五大工具组（官方分类）

### 网格工具（Mesh Tools）（71 项）

```
Transformation
Move, Rotate, Scale
To Sphere
Shear
Bend
Push/Pull
Warp
Randomize
Shrink Fatten
Skin Resize
Mirror
Axis of Symmetry
Pivot Point
Transformation Orientations
Duplicate
Extrude
Extrude Faces
Extrude Faces Along Normals
Extrude Individual Faces
Extrude Manifold
Extrude Edges
Extrude Vertices
Extrude Repeat
Spin
Merge
By Distance
Split
Selection
Faces by Edges
Faces & Edges by Vertices
Separate
Bisect
Examples
Knife Project
Options
Examples
Convex Hull
Symmetrize
Snap to Symmetry
Normals
Flip
Recalculate
Set from Faces
Rotate
Point to Target
```

### 顶点工具（Vertex Tools）（20 项）

```
Extrude Vertices
Bevel Vertices
Options
New Edge/Face from Vertices
Methods
Connect Vertex Path
Connect Vertex Pairs
Rip Vertices
Examples
Limitations
Rip Vertices and Fill
Rip Vertices and Extend
Slide Vertices
Smooth Vertices
Laplacian Smooth
Blend from Shape
Propagate to Shapes
Vertex Groups
Hooks
Make Vertex Parent
```

### 边工具（Edge Tools）（29 项）

```
Extrude Edges
Bevel Edges
Usage
Options
Examples
Bridge Edge Loops
Examples
Screw
Usage
Limitations
Options
Examples
Subdivide
Options
Examples
Subdivide Edge-Ring
Un-Subdivide
Rotate Edge
Edge Slide
Usage
Offset Edge Slide
Loop Cut and Slide
Usage
Options
Edge Data
Edge Crease
Edge Bevel Weight
Mark Seam & Clear Seam
Mark Sharp & Clear Sharp
```

### 面工具（Face Tools）（20 项）

```
Extrude Faces
Extrude Faces Along Normals
Extrude Individual Faces
Inset Faces
Options
Poke Faces
Triangulate Faces
Triangles to Quads
Solidify Faces
Wireframe
Fill
Grid Fill
Beautify Faces
Intersect (Knife)
Intersect (Boolean)
Weld Edges into Faces
Shade Smooth & Flat
Shade Smooth
Shade Flat
Face Data
```

---

## 1.4 三个必须知道的官方 Note

### ① Geometry Smoothing 不等于 Smooth Shading

> 手册在 Laplacian Smooth 条目下明确警告：
> 「**不要把这个工具和平滑着色选项搞混，它们不一样！**
> **这个工具修改网格本身以降低锐度**，而平滑着色只改视觉表现。」

### ② Loop Cut 的两步交互

> 官方：「工具是**交互式、分两步**的：
> ① **预可视化切割**——激活后把光标移到目标边上，**要切的线以品红色标出**。
> **新建的边循环会停在极点（三角面与 n 边形）处。**」

### ③ Clean Up 一组（清理拓扑）

| 工具 | 作用 |
|---|---|
| **Decimate Geometry** | 减面 |
| **Fill Holes** | 补洞 |
| **Make Planar Faces** | 使面共面 |
| **Split Non-Planar Faces** | 切分非共面 |
| **Split Concave Faces** | 切分凹面 |
| **Delete Loose** | 删游离点/边 |
| **Degenerate Dissolve** | 溶解退化几何 |
| **Merge by Distance** | 按距离合并 |

> **★ 这一组是模型越做越乱时的解药**：硬表面建模后常需要清理。

---

## 与其他部分的关系

- **修改器** → 本技能 [ch02-modifiers](ch02-modifiers.md)（57 个）
- **实际项目怎么用这些工具** → `blender-hard-surface` ch02–ch12
- **快捷键按分区全表** → [references/shortcuts-official.md](../references/shortcuts-official.md)
