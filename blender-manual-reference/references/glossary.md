# Blender 术语表（Glossary）

> 出自《Blender 2.92 Manual》Glossary，**官方定义**。共 67 条。

> 只收录**有独立定义的词条**；嵌套子词条归入主词条下。

| 术语 | 官方定义 |
|---|---|
| **A cubic 3D equivalent to the square 2D pixel.** | The name is a combination of the terms “Volumetric” and “Pixel”. |
| **A global lighting method** | that calculates patterns of light and shadow for rendering graphics images from three-dimensional models. |
| **A non-manifold mesh is a mesh in which the structure of** | a non-overlapped surface (based on its connected faces) will not determine |
| **Active** | When many items are selected, the last selected item will be the active one. |
| **Anti-Aliasing** | Is the technique of minimizing Aliasing, by e.g. rendering multiple samples per pixel. |
| **Armature** | An Object consisting of Bones. Used to Rig characters, props, etc. |
| **Axis Angle** | Rotation method where X, Y, and Z correspond to the axis definition, |
| **Bone** | The building block of an Armature. Made up of a Head, Tail |
| **Bump Mapping** | Technique for simulating slight variations in surface height using a grayscale “heightmap” texture. |
| **Catmull-Clark subdivision surface** | on Wikipedia. |
| **Chain of Edges belonging to consecutive Quads.** | An edge loop ends at a pole or a boundary. Otherwise, it is cyclic. |
| **ChromaChrominance** | In general, a resulting image color decomposition, where its (L or Y) luminance channel is separated. |
| **Conversion (Straight/Premultiplied) Alpha** | Conversion between the two alpha types is not a simple operation and can involve data loss, |
| **Convex Face** | Face where, if lines were drawn from each vertex to every other vertex, |
| **DOFDepth of Field** | The distance in front of and behind the subject which appears to be in focus. For any given lens setting, |
| **Data User** | An existing Blender object, which is using its own data, or |
| **Diffuse Light** | Even, directed light coming off a surface. |
| **Directional Light** | The light that has a specific direction, but no location. |
| **Edge** | Straight segment (line) that connects two Vertices, and can be part of a Face. |
| **Empty** | An Object without any Vertices, Edges or Faces. |
| **EulerEuler Rotation** | Rotation method where rotations are applied to each of the X, Y, Z axes in a specific order. |
| **Fake User** | A special Data User, a program construct that is |
| **Frame Types** | In video compression, a frame can be compressed by several different algorithms. |
| **Gimbal Lock** | The limitation where axes of rotation can become aligned, |
| **Luminance** | The intensity of light either in an image/model channel, |
| **MIPMip-mapMip-mapping** | ‘MIP’ is an acronym of the Latin phrase ‘multum in parvo’, meaning ‘much in little’. |
| **Manifold** | Manifold meshes, also called water-tight meshes, define a closed non-self-intersecting volume |
| **MatCap** | Stands for “material capture”, using an image to represent a complete material |
| **Mesh** | Type of object consisting of Vertices, Edges and Faces. |
| **Multisampling** | Rendering multiple samples per pixel, for Anti-Aliasing. |
| **NDOF3D Mouse** | A general term used to describe a 3D mouse, or any input devices which supports |
| **Nonlinear Animation** | Animation technique that allows the animator to edit motions as a whole, |
| **Normal Mapping** | Is similar to Bump Mapping, but instead of the image being a grayscale heightmap, |
| **Object** | Container for a type (mesh, curve, surface, metaball, text, armature, |
| **Object CenterObject Origin** | A reference point used to position, rotate, and scale an Object |
| **Orthographic** | In an orthographic projection, |
| **Particle System** | Technique that simulates certain kinds of fuzzy phenomena, |
| **Pixel** | The smallest unit of information in a 2D raster image, |
| **Pole** | Vertex where three, five, or more edges meet. |
| **Pose Mode** | Used for Posing, Keyframing, Weight Painting, |
| **Posing** | Moving, Rotating and Scaling the Bones of an Armature |
| **Premultiplied Alpha** | Method where RGBA channels are stored as (R × A, G × A, B × A, A), |
| **Primaries** | In color theory, primaries (often known as primary colors) are the abstract lights, |
| **Projection** | In computer graphics, there are two common camera projections used. |
| **Proxy** | For video editing, a proxy is a smaller version of the original file, |
| **QuaternionQuaternion Rotation** | Rotation method where rotations are defined by four values (X, Y, Z, and W). |
| **RGB** | An additive system where three primaries; red, green, and blue are combined to make other colors. |
| **Radiosity (computer graphics)** | on Wikipedia. |
| **Random SeedSeed** | Blender uses pseudo random number generators, which produce numbers that appear to be random, |
| **Ray Tracing** | Rendering technique that works by tracing the path taken by a ray of light through the scene, |
| **Real User** | A Blender object, which is a Data User. |
| **SSSSubsurface Scattering** | Mechanism of light transport in which light penetrates the surface of a translucent object, |
| **Saturation** | Also known as colorfulness, saturation is the quantity of hue in the color |
| **Scanline** | Rendering technique. Much faster than Ray Tracing, |
| **Shading** | Process of altering the color of an object/surface in the 3D scene, |
| **Similar to HSV except the colors are represented as** | Hue, Saturation, and Luminance. |
| **Specular Light** | A light which is reflected precisely, like a mirror. |
| **Straight Alpha** | Method where RGBA channels are stored as (R, G, B, A) |
| **Tail** | A subcomponent of a Bone. Has X, Y and Z coordinates measured in the Local Space |
| **Tangent** | A line that intersects a surface at exactly one point, |
| **Technique for adding more geometry to a mesh.** | It creates new vertices on subdivided edges, new edges between subdivisions and new faces based on new edges. |
| **Topology** | The arrangement of Vertices, Edges, and Faces which define the shape of a mesh. |
| **Transform** | The combination of location, rotation, and scale. |
| **Video Systems** | Refers to the general color decomposition resulting in Y (Luminance) and C (Chrominance) channels, |
| **Walk Cycle** | In animation, a walk cycle is a character that has just the walking function animated. |
| **White Point** | A reference value for white light defined by what happens when all the primaries, |
| **YCbCr** | Luminance-ChannelBlue-ChannelRed component video for digital broadcast use, |

---

## 硬表面建模最常查的术语（摘）

| 术语 | 含义 |
|---|---|
| **Active** | 多选时**最后选中的**那个物品是 active，界面只显示它的选项 |
| **Armature** | 由骨骼（Bones）组成的物体，用于绑定角色、道具 |
| **Bone** | Armature 的构建单元，由 Head、Tail 组成 |
| **Bump Mapping** | 用灰度图**模拟表面高度细微变化**的技术 |
| **Anti-Aliasing** | 通过**每像素多次采样**来最小化锯齿的技术 |
| **Aliasing** | 渲染伪影，表现为**锯齿状线条** |
| **Alpha Channel** | 图像中**用于透明度的额外通道** |
| **Straight Alpha** | RGBA 分别存储，RGB **不受** alpha 影响（PS/GIMP、PNG/BMP/Targa 用） |
| **Premultiplied Alpha** | RGB **已乘过** alpha（渲染引擎的自然输出、OpenEXR 用） |
| **RGB** | 红绿蓝三**加色**原色组合成色的系统 |

> **★ 两条最容易混的**：**Straight vs Premultiplied Alpha**。
> **画图软件/网页输出 = Straight；渲染/合成的中间文件 = Premultiplied。**
> 两者转换**不是简单运算**——手册明确说「is not a simple operation」。
