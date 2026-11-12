# Blender 快捷键与菜单路径总表

> 全部条目**核对过原文出处**（标注章节）。频次来自全书 12 章统计。
> **⚠ 版本提示**：本书写作于 Blender 3.x（2022）。文中出现的快捷键以**书里写的为准**，并标注新旧差异。

---

## 一、最高频 12 条（按全书出现次数）

| 快捷键 | 频次 | 作用 | 出处 |
|---|---|---|---|
| **Alt + S** | **14** | **沿法线缩放/加厚**。原文：「因为没有厚度，我们用 **Alt + S** 并向上移动鼠标给选中的边循环**加厚度**，这会把挤出的面循环向外扩张」 | ch02 |
| **Ctrl + B** | **10** | **倒角（Bevel）**。原文：「选它们的边并**按 Ctrl + B 生成倒角**」 | ch02 |
| **Ctrl + R** | **8** | **环切（Loop Cut）**。原文：「**激活 Loop Cut 工具的快捷键是 Ctrl + R**」 | ch02 |
| **G** | 6 | 移动。**连按两次 G** = 顶点滑移（Vertex Slide） | ch02 |
| **S** | 5 | 缩放。**`S` 后按 `X/Y/Z`** 限定单轴 | ch02 |
| **Shift + N** | 5 | **重算法线（Recalculate Outside）** | ch03 |
| **Shift + D** | 5 | 复制（Duplicate） | ch03 |
| **Shift + W** | 4 | **⚠ 5.1.2 实测：这是 `transform.bend` 弯曲工具，不是合并顶点。** 合并顶点走 **`M` 菜单 → By Distance**（无快捷键） | ch03 |
| **Ctrl + L** | 4 | **关联物体数据（Link Object Data）**。原文：灯光示例，「选所有灯，**最后选中间那盏**，用 **Ctrl + L**」 | ch04 |
| **L** | 3 | **选松散部件**（Linked under cursor）。原文：「悬停在顶点/边/面上**按 L 键**」 | ch01 |
| **P** | 3 | 分离（Separate） | 多章 |
| **Ctrl + J** | 3 | 合并物体（Join）。原文：「用 **Ctrl + J** 把分离的部件与原形重新合并」 | ch05 |

> **★ 版本差异（原文明确）**：
> 「用**整物体在 Edit Mode 下按 `Shift + N`** 来修正法线。」（ch03）
> **✅ 5.1.2 实测确认：重算法线仍是 `Shift + N`**（`mesh.normals_make_consistent`），`Ctrl+Shift+N` 是变体。

---

## 二、视图与选择

| 快捷键 | 作用 | 出处 |
|---|---|---|
| **Numpad 1** | **前视**正交 | ch02 |
| **Numpad 3** | **右视**正交 | ch02 TIP |
| **Numpad 7** | **顶视**正交 | ch02 TIP |
| **Numpad 9** | 切到**当前视图的反面** | ch02 TIP |
| **Ctrl + Numpad 1/3/7** | **后/左/底**视 | ch02 TIP |
| **Tab** | **Object Mode ↔ Edit Mode** | ch02 |
| **1 / 2 / 3**（Edit Mode） | **顶点 / 边 / 面** 选择模式 | ch02 |
| **Alt + 左键**（悬停边） | **选边循环（Select Loop）** | ch01 |
| **L**（悬停） | **选整个松散部件** | ch01 |
| **B** | 框选（Box Select） | ch02 |
| **Ctrl + I** | **反选**。原文：「按 **Ctrl + I 反选**（选所有未选中的、取消所有选中的）」 | ch09 |
| **Shift + G** | **选择相似（Select Similar）**。原文：「选一个面按 **Shift + G**，在 Select Similar 菜单点 **Material**，选所有同材质的面」 | ch06 |

---

## 三、建模核心

| 快捷键 | 作用 | 出处 |
|---|---|---|
| **E** | **挤出**。**`E` 后按 `X/Y/Z`** 限定轴 | ch02 |
| **I** | **内插面（Inset Faces）**。原文：「按 **I** 插入面并挤出」 | ch05 |
| **F** | **连线成面（Make Edge/Face）**。原文：「用 **F** 填面」 | ch05、ch07 |
| **J** | **连接顶点成边（Join）**。原文：「取两个角顶点用 **J** 连成一条边」 | ch03 |
| **Ctrl + T** | **三角化**。原文：「选中面按 **Ctrl + T** 三角化」 | ch07 |
| **Shift + B** | **顶点倒角**。原文：「选顶点用 **Shift + B** 发起倒角」 | ch05 |
| **Ctrl + E** | **边菜单**。原文：「选锐边按 **Ctrl + E**，菜单里选 **Mark Sharp**」 | ch08 |
| **Shift + Y** | **除 Y 轴外等比缩放**（`S` 后按） | ch03 |
| **Shift + X** | **除 X 轴外等比缩放**（`S` 后按） | ch08 |
| **X** | 删除菜单 | ch02 |
| **Shift + W** | **弯曲（transform.bend）** —— 合并顶点请用 `M` 菜单 | ch03 |
| **Ctrl + W** | **翻转法线（Flip Normals）**。原文：「若法线仍未修正，选所有红面**按 Ctrl + W 手动翻转**」 | ch06 |

> **⚠ 实测补充（5.1.2）**：
> | 快捷键 | 编辑模式（Mesh） | 物体模式（Object） |
> |---|---|---|
> | **`Alt-S`** | **沿法线缩放**（`transform.shrink_fatten`）✓ | **清除缩放**（`object.scale_clear`）——不是沿法线！ |
>
> **所以 `Alt-S` 加厚必须在编辑模式里用。**

> **⚠ 易混淆三组**：
> | 快捷键 | 是 | 不是 |
> |---|---|---|
> | **Shift + W** | **弯曲工具**（5.1.2 实测） | 不是合并顶点（那走 `M` 菜单） |
> | **Ctrl + W** | 翻转法线 | 不是"关闭文件" |
> | **Shift + N** | 重算法线 | 不是"新建" |

---

## 四、物体与组织

| 快捷键 | 作用 | 出处 |
|---|---|---|
| **Shift + A** | **添加菜单（Add）** | ch02 |
| **Shift + S** | **Snap 吸附菜单**（含 **Cursor to Selected**） | ch02 |
| **Shift + D** | 复制 | ch03 |
| **Shift + J** | **合并选中的圆（桥接前）**。原文：「若把圆做成独立物体，可选中两者按 **Shift + J** 合并」 | ch03 |
| **Ctrl + J** | 合并物体 | ch05 |
| **Ctrl + P** | **建立父子关系（Parent）**。原文：「选立方体、再选车体，按 **Ctrl + P** 把立方体设为车体的子级」 | ch11 |
| **P** | 分离（Separate） | ch03 |
| **Ctrl + L** | 关联物体数据 | ch04 |

---

## 五、菜单路径（界面操作，非快捷键）

> 书里大量操作走界面，这类**没有快捷键**，只能点菜单。

| 操作 | 菜单路径 |
|---|---|
| **加参考图** | **Shift+A → Image**（Add 菜单的 Image 区）|
| **参考图变半透明** | 选中图 →**右侧 Image Properties 标签**→勾 **Opacity**→拖滑杆 |
| **3D 游标吸附到选中面** | **Shift+S → Cursor to Selected** |
| **视图着色开 Cavity** | 右上 **Viewport Shading** 菜单 → 底部勾 **Cavity** → **Type** 选 **Both** → 所有滑杆拉满 |
| **加修改器** | 右侧 **Modifier Properties 标签**（扳手图标）→ **Add Modifier** |
| **物体属性** | 右侧 **Object Properties**（橙色方块图标） |
| **材质** | 右侧 **Material Properties**（红球图标） |
| **贴图** | 右侧 **Texture Properties**（红白方格图标） |
| **UV 展开** | Edit Mode 全选 → **`U`** → 选展开方式（ch06） |
| **Mark Sharp** | Edit Mode 选边 → **Ctrl+E** → **Mark Sharp**（ch08） |
| **合并顶点** | Edit Mode → **`M`** 菜单 → By Distance（**唯一方式，无快捷键**） |
| **比例编辑开关** | 3D 视图**顶部中间**的 **Proportional Editing Objects** 按钮（ch01） |
| **枢轴点（3D 游标作轴心）** | 3D 视图顶部**枢轴点下拉**→选 **3D Cursor**（ch08 用到） |

---

## 六、修改器快捷键（书里出现的）

| 修改器 | 添加方式 |
|---|---|
| **Mirror** | Modifier Properties → Add Modifier → Generate → **Mirror** |
| **Array** | 同上 → **Array** |
| **Boolean** | 同上 → **Boolean** |
| **Solidify** | 同上 → **Solidify** |
| **Subdivision Surface** | 同上 → **Subdivision Surface** |
| **Curve** | 同上 → Deform → **Curve** |
| **Shrinkwrap** | 同上 → Deform → **Shrinkwrap** |
| **Edge Split** | 同上 → Generate → **Edge Split**（ch10） |

> 详细参数见 [modifiers.md](modifiers.md)。

---

## 七、按任务查快捷键

| 我要… | 快捷键/路径 |
|---|---|
| 进/出编辑模式 | **Tab** |
| 只选顶点/边/面 | **1 / 2 / 3** |
| 选一整圈边 | **Alt + 左键**（悬停边） |
| 选整个部件 | **L**（悬停） |
| 加一圈线段 | **Ctrl + R** |
| 把边上倒角 | **Ctrl + B** |
| 把顶点倒角 | **Shift + B** |
| 拉出一个面 | **E** |
| 面内缩一圈 | **I** |
| 让面沿自身法线加厚 | **Alt + S** |
| 把顶点焊接在一起 | **M 菜单 → By Distance**（`Shift-W` 是弯曲，不焊接） |
| 法线朝外 | **Shift + N** |
| 法线翻转 | **Ctrl + W** |
| 复制一个 | **Shift + D** |
| 把游标吸到选中面 | **Shift + S** → Cursor to Selected |
| 切片沿某轴缩放 | **S** 再按 **X/Y/Z** |
| 选同材质的所有面 | **Shift + G** → Material |
| 反选 | **Ctrl + I** |
| 合并两个物体 | **Ctrl + J** |
| 从一个物体拆出部件 | **P** |
| 设父级 | **Ctrl + P** |
