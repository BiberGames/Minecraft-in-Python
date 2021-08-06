from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import *
from ursina.prefabs.panel import *
from ursina.prefabs.health_bar import *
from configparser import ConfigParser

window.borderless = True    
  
config_file = 'settings.ini'
config_reader = ConfigParser()
config_reader.read(config_file)

save_config = config_reader['game_settings']['save_file']
save_reader = ConfigParser()
save_reader.read(save_config)

texture_config = config_reader['game_settings']['texture_pack']
texture_reader = ConfigParser()
texture_reader.read(texture_config)
print("#########################################################")
print("#  Mini-Minecraft-clone version 3 by:")
print("#                Benjamin (BENJA_303)")
print("#########################################################")
print("# " + config_reader['game_settings']['texture_pack'])
print("# " + config_reader['game_settings']['save_file'])
print("#########################################################")
print("# " + texture_reader['resource']['grass_texture'])
print("# " + texture_reader['resource']['wood_texture'])
print("# " + texture_reader['resource']['stone_texture'])
print("# " + texture_reader['resource']['leave_texture'])
print("# " + texture_reader['resource']['glass_texture'])
print("# " + texture_reader['resource']['bedrock_texture'])
print("# " + texture_reader['resource']['water_texture'])
print("#########################################################")
print("# " + config_reader['game_settings']['world_size'])
print("#########################################################")

game = Ursina()

#Sky()
grass_texture = load_texture(texture_reader['resource']['grass_texture']) 
wood_texture = load_texture(texture_reader['resource']['wood_texture']) 
stone_texture = load_texture(texture_reader['resource']['stone_texture']) 
leave_texture = load_texture(texture_reader['resource']['leave_texture']) 
glass_texture = load_texture(texture_reader['resource']['glass_texture'])
bedrock_texture = load_texture(texture_reader['resource']['bedrock_texture'])
water_texture = load_texture(texture_reader['resource']['water_texture'])
flower1_texture = load_texture(texture_reader['resource']['flower1_texture'])
flower2_texture = load_texture(texture_reader['resource']['flower2_texture'])
flower3_texture = load_texture(texture_reader['resource']['flower3_texture'])
flower4_texture = load_texture(texture_reader['resource']['flower4_texture'])
sun_texture = load_texture(texture_reader['resource']['sun_texture'])
moon_texture = load_texture(texture_reader['resource']['moon_texture'])
debug_texture = load_texture(texture_reader['resource']['debug_texture'])

block_id = 0
block_id = int(save_reader['player']['block'])

def update():
    global block_id

    if held_keys['1']: 
        block_id = 1
    if held_keys['2']: 
        block_id = 2
    if held_keys['3']: 
        block_id = 3
    if held_keys['4']: 
        block_id = 4
    if held_keys['5']: 
        block_id = 5
    if held_keys['6']: 
        block_id = 6
    if held_keys['7']: 
        block_id = 7

    if player.y < -5:
        player.x = random.randint(3, 12) 
        player.y = random.randint(3, 12)
        player.z = random.randint(3, 12)

class Water_Voxel(Button):
    def __init__(self, position = (0,0,0), texture = water_texture, model='cube'):
        print(position, block_id, model, texture)
        super().__init__(
            parent = scene,
            position = position,
            model = model,
            origon_y = 0,
            texture = texture,
            color = color.white,
            highlight_color=color.white,
            collider = 'plane'
            )

    def update(self):
        if self.y > 1:
            self.y = self.y - 0.5
            Wait(1000)

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                if block_id == 0: border = Border(position = self.position + mouse.normal)
                if block_id == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_id == 2: voxel = Voxel(position = self.position + mouse.normal, texture = wood_texture)
                if block_id == 3: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_id == 4: voxel = Voxel(position = self.position + mouse.normal, texture = leave_texture)
                if block_id == 5: voxel = Voxel(position = self.position + mouse.normal, texture = glass_texture)
                if block_id == 6: tree = summonTree(position = self.position + mouse.normal)
                if block_id == 7: water_voxel = Water_Voxel(position = self.position + mouse.normal, texture = water_texture)
                
            if key == 'left mouse down':
                destroy(self)

class Border(Button):
    def __init__(self, position = (0,0,0)):
        print(position, block_id, texture)
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origon_y = 0,
            texture = bedrock_texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            )

    def input(self, key):
       if self.hovered:
            if key == 'right mouse down':
                if block_id == 0: border = Border(position = self.position + mouse.normal)
                if block_id == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_id == 2: voxel = Voxel(position = self.position + mouse.normal, texture = wood_texture)
                if block_id == 3: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_id == 4: voxel = Voxel(position = self.position + mouse.normal, texture = leave_texture)
                if block_id == 5: voxel = Voxel(position = self.position + mouse.normal, texture = glass_texture)
                if block_id == 6: tree = summonTree(position = self.position + mouse.normal)
                if block_id == 7: water_voxel = Water_Voxel(position = self.position + mouse.normal, texture = water_texture)

            if key == 'left mouse down':
                print("not today!")
                #destroy(self)
                pass

class grass_Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture, model='cube', collider = 'cube'):
        print(position, block_id, model, texture)
        super().__init__(
            parent = scene,
            position = position,
            model = model,
            origon_y = 0,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color=color.white,
            collider = collider
            )
    
    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                destroy(self)
            if key == 'left mouse down':
                destroy(self)

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture, model='cube', collider = 'cube'):
        print(position, block_id, model, texture)
        super().__init__(
            parent = scene,
            position = position,
            model = model,
            origon_y = 0,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color=color.white,
            collider = collider
            )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                if block_id == 0: border = Border(position = self.position + mouse.normal)
                if block_id == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_id == 2: voxel = Voxel(position = self.position + mouse.normal, texture = wood_texture)
                if block_id == 3: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_id == 4: voxel = Voxel(position = self.position + mouse.normal, texture = leave_texture)
                if block_id == 5: voxel = Voxel(position = self.position + mouse.normal, texture = glass_texture)
                if block_id == 6: tree = summonTree(position = self.position + mouse.normal)
                if block_id == 7: water_voxel = Water_Voxel(position = self.position + mouse.normal, texture = water_texture)
            if key == 'left mouse down':
                destroy(self)
         
        if key == 'escape':
            print("saving...")
            floor(player.x)
            floor(player.y)
            floor(player.z)
            f = open(save_config, "w")
            f.write("[player]\n")
            f.write("block = " + str(block_id)+("\n"))
            f.write("px = " + str(player.x)+("\n"))
            f.write("py = " + str(player.y)+("\n"))
            f.write("pz = " + str(player.z)+("\n"))
            f.close()
            print("house_random: ", house_random)
            print("bay!")
            quit()

class Chunk(Entity):
    def __init__(self, sa, sb, sc,sd):
        for bx in range(int(config_reader['game_settings']['world_size'])):
            for bz in range(int(config_reader['game_settings']['world_size'])):
                border = Border(position = (bx + sa,-2,bz + sc))
        for x in range(int(config_reader['game_settings']['world_size'])):
            for z in range(int(config_reader['game_settings']['world_size'])):
                voxel = Voxel(position = (x+sa,+sb,z+sc))
                for y in range(1):  
                    voxel = Voxel(position = (x+sa,y-sd+sb,z+sc), texture = stone_texture)

class grass(Entity):
    def __init__(self, sa, sb, sc,sd):
        for bx in range(int(config_reader['game_settings']['world_size'])):
            for bz in range(int(config_reader['game_settings']['world_size'])):
                grass_random = random.randint(0, 6)
                grass_random_texture = random.randint(1, 4)
                if grass_random_texture == 1:
                    flower_texture = flower1_texture
                if grass_random_texture == 2:
                    flower_texture = flower2_texture
                if grass_random_texture == 3:
                    flower_texture = flower3_texture
                if grass_random_texture == 4:
                    flower_texture = flower4_texture
                if grass_random == 6:
                    grass = grass_Voxel(position = (bx + sa,0.51,bz + sc), texture = flower_texture, model = 'plane', collider = 'plane')
                    
class House(Entity):
    def __init__(self, ha, hb):
        l1 = Voxel(position = (ha, 1, hb), texture = stone_texture)
        l1 = Voxel(position = (ha+1, 1, hb), texture = stone_texture)
        l1 = Voxel(position = (ha+1, 1, hb+1), texture = stone_texture)
        l1 = Voxel(position = (ha+1, 1, hb+2), texture = stone_texture)
        l1 = Voxel(position = (ha+1, 1, hb+3), texture = stone_texture)
        l1 = Voxel(position = (ha+1, 1, hb+4), texture = stone_texture)
        l1 = Voxel(position = (ha+1, 1, hb+5), texture = stone_texture)
        l1 = Voxel(position = (ha, 1, hb+5), texture = stone_texture)
        l1 = Voxel(position = (ha-1, 1, hb+5), texture = stone_texture)
        l1 = Voxel(position = (ha-2, 1, hb+5), texture = stone_texture)
        l1 = Voxel(position = (ha-3, 1, hb+5), texture = stone_texture)
        l1 = Voxel(position = (ha-3, 1, hb+4), texture = stone_texture)
        l1 = Voxel(position = (ha-3, 1, hb+3), texture = stone_texture)
        l1 = Voxel(position = (ha-3, 1, hb+2), texture = stone_texture)
        l1 = Voxel(position = (ha-3, 1, hb+1), texture = stone_texture)
        l1 = Voxel(position = (ha-3, 1, hb), texture = stone_texture)
        l1 = Voxel(position = (ha-2, 1, hb), texture = stone_texture)

        for y in range(2):
            l1 = Voxel(position = (ha, y+2, hb), texture = wood_texture)
            l1 = Voxel(position = (ha+1, y+2, hb), texture = wood_texture)
            l1 = Voxel(position = (ha+1, y+2, hb+1), texture = wood_texture)
            l1 = Voxel(position = (ha+1, y+2, hb+2), texture = glass_texture)
            l1 = Voxel(position = (ha+1, y+2, hb+3), texture = glass_texture)
            l1 = Voxel(position = (ha+1, y+2, hb+4), texture = wood_texture)
            l1 = Voxel(position = (ha+1, y+2, hb+5), texture = wood_texture)
            l1 = Voxel(position = (ha, y+2, hb+5), texture = wood_texture)
            l1 = Voxel(position = (ha-1, y+2, hb+5), texture = glass_texture)
            l1 = Voxel(position = (ha-2, y+2, hb+5), texture = wood_texture)
            l1 = Voxel(position = (ha-3, y+2, hb+5), texture = wood_texture)
            l1 = Voxel(position = (ha-3, y+2, hb+4), texture = wood_texture)
            l1 = Voxel(position = (ha-3, y+2, hb+3), texture = wood_texture)
            l1 = Voxel(position = (ha-3, y+2, hb+2), texture = glass_texture)
            l1 = Voxel(position = (ha-3, y+2, hb+1), texture = glass_texture)
            l1 = Voxel(position = (ha-3, y+2, hb), texture = wood_texture)
            l1 = Voxel(position = (ha-2, y+2, hb), texture = wood_texture)

        for x in range(5):
            for z in range(6):
                l4 = Voxel(position = (x+ha-3, 4, z+hb), texture = wood_texture)

class summonTree(Entity):
    def __init__(self, position=(0,0,0)):
        tree = Tree(position.x, position.z)

class Tree(Entity):
    def __init__(self, a, b):
        for y in range(3):
            samp = Voxel(position = (a, 1 + y, b), texture = wood_texture)

        for y in range(2):
            for x in range(1): 
                levae2 = Voxel(position = (a - 1, y + 4, b), texture = leave_texture)
                levae3 = Voxel(position = (a - 1, y + 4, b -1 ), texture = leave_texture)
                levae4 = Voxel(position = (a + 1, y + 4, b), texture = leave_texture)
                levae5 = Voxel(position = (a + 1, y + 4, 1 + b), texture = leave_texture)
                levae6 = Voxel(position = (a, y + 4, b + 1), texture = leave_texture)
                levae7 = Voxel(position = (a - 1, y + 4, b + 1), texture = leave_texture)
                levae8 = Voxel(position = (a + 1, y + 4, b - 1), texture = leave_texture)
                levae9 = Voxel(position = (a, y + 4, b - 1), texture = leave_texture)
                levae10 = Voxel(position = (a, y + 5, b), texture = leave_texture)

playerx = int(float(save_reader['player']['px']))
playery = 4 #int(float(save_reader['player']['py']) + 1)
playerz = int(float(save_reader['player']['pz']))

print(save_reader['player']['px'] + "/" + save_reader['player']['py'] + "/" + save_reader['player']['pz'])
player = FirstPersonController(x=playerx,y=playery,z=playerz,jump_height=1,speed=5, size_y=1.5)

chunk1 = Chunk(0,0,0,1)
for i in range(random.randint(0, 4)):
    tree = Tree(random.randint(0, 22), random.randint(0, 22))
grass = grass(0,0,0,1)
house_random = random.randint(0, 303)
print("house_random: ", house_random)
if house_random == 283:
    house = House(10,15)

sun = Entity(model = 'plane', texture = sun_texture, position = (9.5, 200, 9.5), rotation = (180, 0, 0), scale = 20)
#moon = Entity(model = 'plane', texture = moon_texture, position = (9.5, 200, 9.5), rotation = (180, 0, 0), scale = 15)

border_water = Entity(y = -2, model='plane', texture=water_texture, scale=303, roundness=100, color = color.white)
boreder_bedrock = Entity(y = -3, model='plane', color=color.white, scale=303, roundness=100, texture = bedrock_texture, collider = 'plane')


Sky()
game.run()