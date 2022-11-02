import json

class SceneFactory:
    
    def __init__(self):
            self.rows = 10
            self.columns = 16
            self.maze = [   1,1,1,1,1,1,1,1,1,1,
                            1,0,0,0,0,0,0,0,0,1,
                            1,0,1,0,1,0,1,1,0,1,
                            1,0,1,0,0,0,0,1,0,1,
                            1,0,1,1,0,1,0,1,0,1,
                            1,0,0,0,0,0,0,0,0,1,
                            1,0,1,0,1,0,1,1,0,1,
                            1,0,0,0,1,0,0,0,0,1,
                            1,0,1,0,1,0,1,1,0,1,
                            1,0,0,0,0,0,0,0,0,1,
                            1,0,1,1,1,0,1,1,0,1,
                            1,0,1,0,0,0,1,1,0,1,
                            1,0,0,0,1,0,0,0,0,1,
                            1,0,1,0,1,0,1,1,0,1,
                            1,0,0,0,0,0,0,0,0,1,
                            1,1,1,1,1,1,1,1,1,1,]
    
    def saveSceneFromFile(self, fileName):
        with open(fileName, "r+") as f:
            try:
                # this is a dictionary
                k = json.load(f)
                
            except Exception as e:
                print(f"Error on filename : {fileName}")
                print(str(e))
        
        window = k['window']
        actors=k["actors"]
        
        
        def set_component_in_actor(n_actor):
            components_actor=actors[n_actor]["components"]
            
            return components_actor
            
        
        def edit_window(height, width, dict=dict()):
            window["width"] = width
            window["height"] = height
            window.update(dict)
            
            
        def new_actor():
            new_actor= k["actors"]
            actor= {
            "name": "",
            "x": 0,
            "y": 0,
            "type": None,
            "components": [{
                    "name": "",
                    "type": "",
                    }
            
                ]
            }
            new_actor.append(actor)
        
        
        def edit_actor(name, x, y, n_actor):
            actors[n_actor]["name"]=name
            actors[n_actor]["x"]=x
            actors[n_actor]["y"]=y
            
        def edit_type(n_actor, type):
             actors[n_actor]["type"]=type
           
            
        def new_component(n_actor):
            components_actor= set_component_in_actor(n_actor)
            component= {
                "name": "",
                "type": "",
            }
            components_actor.append(component)
        
        
        
        def edit_component(name, type, n_actor, n_component, dict=dict()):
            components_actor= set_component_in_actor(n_actor)
            components_actor[n_component]["name"]=name
            components_actor[n_component]["type"]=type
            components_actor[n_component].update(dict)
            
            
            
        def add_to_component(n_actor, n_component, dict=dict()):
            components_actor= set_component_in_actor(n_actor)
            components_actor[n_component].update(dict)
            
            
            
        
        
        with open(fileName, "w") as g:   
            
            x = 0
            y = 0
            counter = 0
            
            #add actor
            new_actor()
            #write second actor
            edit_actor("maze", 0, 0, counter)
            
            #write first component in maze actor
            edit_component("maze", "pacman.components.DrawMazeComponent", counter, 0, {"fileName": "pacman/assets/img/blu_square.png"})
            
            counter+=1 
            
            #add actor ghost
            new_actor()
            #write second actor
            edit_actor("ghost", 0, 0, counter)
            
            edit_type(counter, "pacman.actors.Ball")
            
            edit_component("movement", "pacman.components.BallMovementComponent", counter, 0, {"speed": 50})
            
            add_to_component(counter, 0, {"AABB": { "x": 0, "y": 0, "width": 35, "height": 35 }})
            
            
            edit_component("sprite", "engine.components.StaticSpriteComponent", counter, 1, {"fileName": "pacman/assets/img/ghost1.png"})
            
            
            counter += 1
            
            #add actor player
            new_actor()
            #write second actor
            edit_actor("player", 0, 0, counter)
            
            edit_component("sprite", "engine.components.AnimatedSpriteComponent", counter, 0, {"pingPong": True})
            
            add_to_component(counter, 0, {"frames": [
                        { "fileName": "pacman/assets/img/pacman_open.png", "duration": 0.1 },
                        { "fileName": "pacman/assets/img/pacman_close.png", "duration": 0.1 }
                    ]})
            
            new_component(counter)
            
            edit_component("movement", "pacman.components.PlayerMovementComponent", counter, 1, {"speed": 150})
            
            add_to_component(counter, 1, {"inertia": 400,})
            
            add_to_component(counter, 1, {"AABB": { "x": 0, "y": 0, "width": 32, "height": 32 }})
            
            
            counter += 1
            
            for i in range(0, len(self.maze)):
                    if self.maze[i] == 1:
                        rx = x * 40
                        ry = y * 40
                        #add actor
                        new_actor()
                        #write second actor
                        edit_actor("brick", rx, ry, counter)
                        
                        #write first component in second actor
                        edit_component("collision", "engine.components.ColliderComponent", counter, 0, {"AABB": { "x": rx, "y": ry, "width": 40, "height": 40 }})
                        
                        new_component(counter)
                        
                        edit_component("sprite", "engine.components.StaticSpriteComponent", counter, 1, {"fileName": "pacman/assets/img/blu_square.png"})
                        
                        counter += 1
                    #coordinate for blit
                    x += 1
                    if x > self.rows-1:
                        x = 0 
                        y += 1
            

            k=json.dump(k, g)