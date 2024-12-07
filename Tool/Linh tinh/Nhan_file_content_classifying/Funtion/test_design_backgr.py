from ursina import *
app = Ursina()

# Tạo tường
wall = Entity(model='cube', color=color.gray, scale=(5, 5, 0.5), position=(0, 0, 3))

# Tạo bậc thang
step1 = Entity(model='cube', color=color.dark_gray, scale=(1, 0.3, 1), position=(0, -1, 2))
step2 = Entity(model='cube', color=color.dark_gray, scale=(1, 0.3, 1), position=(0, -0.7, 1.5))

# Tạo rương vàng
chest = Entity(model='cube', color=color.gold, scale=(0.5, 0.5, 0.5), position=(0, -0.4, 1))

# Tạo ánh sáng
light = PointLight(position=(0, 2, 0), color=color.orange)

# Camera và môi trường
camera.position = (0, 1, -5)

app.run()
