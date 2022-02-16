from mcpi.minecraft import Minecraft
servidor = Minecraft.create()

def casa(jugador):
    posicion = servidor.entity.getPos(jugador)
    servidor.setBlocks(posicion.x-4,posicion.y-1,posicion.z-4,posicion.x+4,posicion.y-1,posicion.z+4,24)
    servidor.setBlocks(posicion.x-4,posicion.y+4,posicion.z-4,posicion.x+4,posicion.y+4,posicion.z+4,24)
    for altura in range(4):
        for barrahor in range(-4,5,8):
            for barra in range(-4,5):
                servidor.setBlock(posicion.x+barrahor,posicion.y+altura,posicion.z+barra,24)
                servidor.setBlock(posicion.x+barra,posicion.y+altura,posicion.z+barrahor,24)
    servidor.setBlock(posicion.x,posicion.y,posicion.z+4,0)
    servidor.setBlock(posicion.x,posicion.y+1,posicion.z+4,0)
    servidor.setBlock(posicion.x,posicion.y,posicion.z+4,64,0)
    servidor.setBlock(posicion.x,posicion.y+1,posicion.z+4,64,8)
    servidor.setBlock(posicion.x-3,posicion.y+2,posicion.z,50,1)
    servidor.setBlock(posicion.x+3,posicion.y+2,posicion.y,50,2)
    servidor.setBlock(posicion.x,posicion.y+2,posicion.z-3,50,3)
    servidor.setBlock(posicion.x,posicion.y+2,posicion.z+3,50,4)
    servidor.postToChat('Casa construida!!!')
while (True):
    mensajes = servidor.events.pollChatPosts()

    if mensajes:
        for mensaje in mensajes:
            if mensaje.message =='!construye_casa':
                casa(mensaje.entityId)