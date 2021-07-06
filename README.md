# Python-Interception-Driver

http://www.oblita.com/interception

### Example:
```py
#from interception import Interception, MouseFilter, keyFilter, MouseFlags,\
#    MouseState, KeyState, MapVk, Vk, map_virtual_key

RUNNING = True
TIMEOUT = 2500 # ms

interception = Interception()

interception.set_mouse_filter(MouseFilter.ButtonAll)
interception.set_keyboard_filter(KeyFilter.All)

while RUNNING:
    device = interception.wait_receive(TIMEOUT)

    if device:
        print(f'{device.get_hardware_id()}:')

        # Mouse
        if device.is_mouse:
            print('MouseStroke(flags={1},state={2},rolling={0.rolling},x={0.x},y={0.y},info={0.info})'
                  .format(device.stroke, MouseFlags(device.stroke.flags), MouseState(device.stroke.state)))

        # Keyboard
        elif device.is_keyboard:
            vk = map_virtual_key(device.stroke.code, MapVk.ScToVk)
            print('KeyStroke(sc={0.code:03X},vk={2:03X},state={1},info={0.info})'
                  .format(device.stroke, KeyState(device.stroke.state), vk))
            # escape = terminate
            if vk == Vk.Escape:
                RUNNING = False
            # switch x and y
            elif vk == Vk.X:
                device.stroke.code = map_virtual_key(Vk.Y, MapVk.VkToSc)
            elif vk == Vk.Y:
                device.stroke.code = map_virtual_key(Vk.X, MapVk.VkToSc)

        device.send()
        print('-'*100)
```
