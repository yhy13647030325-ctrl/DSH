# Blender 版本差异：2.92 ↔ 5.1 实测对照

> **本文有两类证据，必须分清：**
> - **【手册 2.92】** = 从官方手册原文核实
> - **【实测 5.1.2】** = 在运行中的 Blender 5.1.2 GUI 里读 keyconfig / RNA 得到，**可复现**
>
> **实测方法**（任何人都能复验）：
> ```python
> import bpy
> kc = bpy.context.window_manager.keyconfigs.active
> # 注意：必须 GUI 运行；后台模式只有 12 条 keymap_items（实测值），不可用
> ```
> 本次实测：**5.1.2 / keyconfig "Blender" / 284 个 keymap / 3182 个 keymap_items**

---

## 结论速览（六条实测纠正）

| # | 项 | 手册 2.92 | **实测 5.1.2** | 结论 |
|---|---|---|---|---|
| 1 | **重算法线** | `Shift-N` | **`Shift-N`** | ❗**没有变**，我一直写错了 |
| 2 | **Auto Smooth** | Object Data 里的复选框 | **已移除**，改为 `Shade Auto Smooth` → 挂「按角度平滑」几何节点修改器 | 确实变了 |
| 3 | **Shift-W** | 手册未给 Hotkey（Merge by Distance 走菜单） | **`transform.bend`（弯曲）** | 不是合并顶点 |
| 4 | **Alt-S** | 沿法线缩放（Mesh） | Mesh 里是 `transform.shrink_fatten`；**Object Mode 里是清除缩放** | 分模式，含义不同 |
| 5 | **View Transform 默认** | Filmic | **AgX** | 变了 |
| 6 | **Principled 输入** | 20 项 | **31 项**，全套改名 | 变了 |

---

## 1. 重算法线：`Shift-N`（此前写错，已纠正）

**实测输出**：
```
### mesh.normals_make_consistent
    Mesh | Shift+N        active: True
    Mesh | Ctrl+Shift+N   active: True
```

**【实测 5.1.2】** 重算法线仍然是 **`Shift-N`**，`Ctrl+Shift-N` 是另一个变体。

> **❗ 纠错**：我之前在 `version-differences.md` 里写「2.92 `Shift-N` → 3.x/4.x `Ctrl-N`」，
> **这是错的**。实测 5.1.2 里 `Ctrl-N` **不是**重算法线。
> 而 `blender-hard-surface` 里写「**Ctrl + N（新版），Shift + N（旧版）**」——**这句也错了**，
> 至少对 5.1.2 不成立。**正确用法：`Shift-N` 重算法线朝外。**

**已实测确认不受影响的（与手册一致）**：

| 操作 | 算子 | 实测键位 |
|---|---|---|
| 沿法线缩放 | `transform.shrink_fatten` | **`Alt-S`** |
| 环切 | `mesh.loopcut_slide` | **`Ctrl-R`** |
| 倒角（边） | `mesh.bevel` | **`Ctrl-B`** |
| 倒角（顶点） | — | **`Ctrl-Shift-B`** |
| 内插面 | `mesh.inset` | **`I`** |
| 挤出 | `view3d.edit_mesh_extrude_move_normal` | **`E`** |
| 连线成面 | `mesh.edge_face_add` | **`F`** |
| 连接顶点路径 | `mesh.vert_connect_path` | **`J`** |
| 选松散部件 | `mesh.select_linked_pick` | **`L`**（`Shift-L` 加选） |
| 选全部相连 | `mesh.select_linked` | **`Ctrl-L`** |
| 分离 | `mesh.separate` | **`P`** |
| 三角化 | `mesh.quads_convert_to_tris` | **`Ctrl-T`** |
| 顶点撕开 | `mesh.rip_move` | **`V`** / `Alt-V` |
| 边撕开 | `mesh.rip_edge_move` | **`Alt-D`** |
| 镜像 | `transform.mirror` | **`Ctrl-M`** |
| 转球 | `transform.tosphere` | **`Shift-Alt-S`** |
| 复制 | `mesh.duplicate_move` | **`Shift-D`** |

---

## 2. `Shift-W` 是弯曲，不是合并顶点（重要纠正）

**实测输出**：
```
### Mesh
   SHIFT+W   transform.bend        active=True
### transform.bend 键位：
   Curve | SHIFT+W
   Mesh  | SHIFT+W
   Lattice | SHIFT+W
```

**【实测 5.1.2】** `Shift-W` = **`transform.bend`（弯曲工具）**。

**合并顶点去哪了**：
```
### Mesh 中 M 的菜单内容是：
   menu: VIEW3D_MT_edit_mesh_merge
   menu: VIEW3D_MT_edit_mesh_split
```
**【实测】** 合并走 **`M` 菜单**（`VIEW3D_MT_edit_mesh_merge`），**没有直接快捷键**。
实测 `mesh.remove_doubles` 在全键位表里**无任何键位**。

**【手册 2.92】佐证**：2.92 手册的 `Merge by Distance` 条目只写
> `Menu: Vertex ‣ Merge by Distance, Context Menu ‣ Merge by Distance`

**也没有列 Hotkey**。

> **❗ 纠错**：`blender-hard-surface` ch03 写的「**按 `Shift + W` 按距离合并顶点**」**是错的**。
> 那是 2.80 以前的旧键位（当时叫 Remove Doubles）。**正确做法：`M` 菜单 → By Distance。**

---

## 3. `Alt-S` 分模式，含义不同

**实测**：

| 模式 | `Alt-S` 实际是 |
|---|---|
| **Mesh（编辑模式）** | `transform.shrink_fatten`（**沿法线缩放**）✓ |
| **Object Mode** | **`object.scale_clear`（清除缩放）** |

> **实操提醒**：`Alt-S` 必须在**编辑模式**里用才是"沿法线加厚"。
> 在物体模式按 `Alt-S` 是**清空缩放值**，会改变物体变换。

---

## 4. Auto Smooth：复选框已移除，改为几何节点修改器

**【实测 5.1.2】**
```
has use_auto_smooth: False
has auto_smooth_angle: False
shade 相关算子: ['shade_auto_smooth', 'shade_smooth', 'shade_smooth_by_angle', ...]
```

执行 `bpy.ops.object.shade_auto_smooth()` 的结果：
```
modifier: 按角度平滑 | type: NODES
node_group: Smooth by Angle
```

**该修改器暴露给用户的输入**：
```
Mesh          | default: None
Angle         | default: 0.5235987901687622   ← 30°
Ignore Sharpness | default: False
```

**【实测】** 修改器面板上的 **`Angle` 默认 = 0.5236 rad = 30°**，还有 **`Ignore Sharpness`**（忽略锐边标记）开关。

> **对照 `blender-hard-surface`**：它说「**大多数情况下 45 度是最好的角度**」（引自 2.92 手册）。
> **在 5.1.2 里新挂上的修改器默认值是 30°**，不是 45°。
> **所以照那本书做，需要手动把 Angle 从 30 改成 45。**

**【手册 2.92】** 当时的路径是 **Properties ‣ Object Data ‣ Normals** 的复选框 + Angle 值。

---

## 5. 色彩管理：AgX 已成为默认，且新增选项

**【实测 5.1.2】** 逐个尝试赋值，全部成功：
```
OK   Standard
OK   Filmic
OK   AgX                 ← 当前默认
OK   Filmic Log
OK   Raw
OK   False Color
OK   Khronos PBR Neutral  ← 新增
NO   AgX Punchy
```

**默认值实测**：`scene.view_settings.view_transform == "AgX"`

> **对比**：2.92 手册里 **`AgX` 出现 0 次**，默认是 **Filmic**。
> 5.1.2 是 **7 种可选、默认 AgX**，并多出 **Khronos PBR Neutral**。

---

## 6. Principled BSDF：20 项 → 31 项

**【实测 5.1.2】完整 31 项输入**：
```
Base Color / Metallic / Roughness / IOR / Alpha / Normal / Weight /
Diffuse Roughness /
Subsurface Weight / Subsurface Radius / Subsurface Scale / Subsurface IOR / Subsurface Anisotropy /
Specular IOR Level / Specular Tint /
Anisotropic / Anisotropic Rotation / Tangent /
Transmission Weight /
Coat Weight / Coat Roughness / Coat IOR / Coat Tint / Coat Normal /
Sheen Weight / Sheen Roughness / Sheen Tint /
Emission Color / Emission Strength /
Thin Film Thickness / Thin Film IOR
```

**改名对照（实测确认）**：

| 2.92 | 5.1.2 |
|---|---|
| Specular | **Specular IOR Level** |
| Transmission | **Transmission Weight** |
| Clearcoat | **Coat Weight** |
| Clearcoat Roughness | **Coat Roughness** |
| Clearcoat Normal | **Coat Normal** |
| Sheen | **Sheen Weight** |
| Subsurface | **Subsurface Weight** |
| Emission | **Emission Color** |

**新增的（2.92 没有）**：
`Weight`、`Diffuse Roughness`、`Subsurface Scale`、`Subsurface IOR`、`Subsurface Anisotropy`、
`Anisotropic Rotation`、`Coat IOR`、`Coat Tint`、`Sheen Roughness`、`Thin Film Thickness`、`Thin Film IOR`

> **实操影响**：照 2.92 教程说「把 Specular 调到 0.5」，
> 在 5.1.2 里要找 **Specular IOR Level**，**且不是简单改名——语义已改为"IOR 基础上的层级"**。

---

## 7. EEVEE：Bloom 与 GTAO 已移除

**【实测 5.1.2】** `scene.eevee` 共 **56 个属性**，关键检查：
```
bloom: []          ← 无 bloom 属性
gtao:  []          ← 无 gtao 属性
raytrace: ['ray_tracing_method','ray_tracing_options','use_raytracing']   ← 有
volumetric: [9 个]  ← 有
taa: ['taa_render_samples','taa_samples','use_taa_reprojection']  ← 有
fast_gi: [7 个]     ← 新增
```

| 2.92 有 | 5.1.2 | 说明 |
|---|---|---|
| **Bloom** | **移除** | 需用合成器的 **Glare** 节点 |
| **SSR（Screen Space Reflections）** | 改为 **Raytracing**（`use_raytracing`） | |
| **GTAO（Ambient Occlusion）** | **移除**，改为 `use_fast_gi` 一组 | |
| Volumetrics | 保留 | |
| TAA | 保留 | |

---

## 8. 对两个技能的具体修正

| 位置 | 原来写的 | 应改为 |
|---|---|---|
| `blender-manual-reference/references/version-differences.md`（旧版） | 2.92 `Shift-N` → 3.x/4.x `Ctrl-N` | **`Shift-N` 一直是重算法线**（5.1.2 实测）；`Ctrl-N` 不是 |
| `blender-hard-surface` ch03（F-B3-09 等） | 「按 `Shift+W` 按距离合并顶点」 | **`M` 菜单 → By Distance**；`Shift-W` 是**弯曲** |
| `blender-hard-surface` ch03 | 「Auto Smooth 45 度」 | 5.1.2 默认 **30°**，需手动改 45 |
| 两本的 Alt-S 说明 | 「沿法线缩放」 | **仅在编辑模式**；物体模式是清除缩放 |

---

## 9. 复验方法（可自行跑）

```python
import bpy
kc = bpy.context.window_manager.keyconfigs.active

# 查某算子的真实键位
def keys(opname):
    out=[]
    for km in kc.keymaps:
        for i in km.keymap_items:
            if i.idname != opname: continue
            k=("Ctrl+" if i.ctrl else "")+("Shift+" if i.shift else "")+("Alt+" if i.alt else "")+i.type
            out.append((km.name,k))
    return out

print(keys("mesh.normals_make_consistent"))   # [('Mesh','Shift+N'), ('Mesh','Ctrl+Shift+N')]
print(keys("mesh.remove_doubles"))            # []  ← 合并顶点无快捷键
print(keys("transform.bend"))                 # [('Mesh','Shift+W'), ...]

# 查 Principled 输入
m = bpy.data.materials.new("t"); m.use_nodes=True
for n in m.node_tree.nodes:
    if n.type=='BSDF_PRINCIPLED':
        print([i.name for i in n.inputs])
```

> **⚠ 前提**：**必须在 GUI 里跑**。
> 实测后台模式（`--background`）只有 **12 个 keymap_items**（总数应 3182），**读不到真实键位**。
