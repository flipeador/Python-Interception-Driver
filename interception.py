from ctypes import *
from ctypes.wintypes import *
from typing import Final
from enum import IntEnum, IntFlag

INVALID_HANDLE_VALUE: Final = HANDLE(-1).value

WAIT_TIMEOUT        : Final = 0x00000102  # the time-out interval elapsed
WAIT_FAILED         : Final = 0xFFFFFFFF  # error

INFINITE            : Final = 0xFFFFFFFF

IOCTL_SET_PRECEDENCE : Final = 0x222004
IOCTL_GET_PRECEDENCE : Final = 0x222008
IOCTL_SET_EVENT      : Final = 0x222040
IOCTL_SET_FILTER     : Final = 0x222010
IOCTL_GET_FILTER     : Final = 0x222020
IOCTL_READ           : Final = 0x222100
IOCTL_WRITE          : Final = 0x222080
IOCTL_GET_HARDWARE_ID: Final = 0x222200

MIN_DEVICE  : Final = 1
MAX_DEVICE  : Final = 20
MIN_KEYBOARD: Final = 1
MAX_KEYBOARD: Final = 10
MIN_MOUSE   : Final = 11
MAX_MOUSE   : Final = 20

class MapVk(IntEnum):
    VkToSc   = 0
    ScToVk   = 1
    VkToChar = 2
    ScToVkEx = 3
    VkToScEx = 4

class Vk(IntEnum):
    Modifiers          = -65536  # The bitmask to extract modifiers from a key value.
    NoKey              = 0       # No key pressed.
    LeftButton         = 1       # The left mouse button.
    RightButton        = 2       # The right mouse button.
    Cancel             = 3       # The CANCEL key.
    MiddleButton       = 4       # The middle mouse button (three-button mouse).
    XButton1           = 5       # The first x mouse button (five-button mouse).
    XButton2           = 6       # The second x mouse button (five-button mouse).
    Back               = 8       # The BACKSPACE key.
    BackSpace          = 8       # The BACKSPACE key.
    Tab                = 9       # The TAB key.
    LineFeed           = 10      # The LINEFEED key.
    Clear              = 12      # The CLEAR key.
    Return             = 13      # The RETURN key.
    Enter              = 13      # The ENTER key.
    ShiftKey           = 16      # The SHIFT key.
    ControlKey         = 17      # The CTRL key.
    Menu               = 18      # The ALT key.
    Pause              = 19      # The PAUSE key.
    Capital            = 20      # The CAPS LOCK key.
    CapsLock           = 20      # The CAPS LOCK key.
    KanaMode           = 21      # The IME Kana mode key.
    HanguelMode        = 21      # The IME Hanguel mode key.
    HangulMode         = 21      # The IME Hangul mode key.
    JunjaMode          = 23      # The IME Junja mode key.
    FinalMode          = 24      # The IME final mode key.
    HanjaMode          = 25      # The IME Hanja mode key.
    KanjiMode          = 25      # The IME Kanji mode key.
    Escape             = 27      # The ESC key.
    IMEConvert         = 28      # The IME convert key.
    IMENonconvert      = 29      # The IME nonconvert key.
    IMEAccept          = 30      # The IME accept key.
    IMEAceept          = 30      # The IME accept key.
    IMEModeChange      = 31      # The IME mode change key.
    Space              = 32      # The SPACEBAR key.
    PageUp             = 33      # The PAGE UP key.
    Next               = 34      # The PAGE DOWN key.
    PageDown           = 34      # The PAGE DOWN key.
    End                = 35      # The END key.
    Home               = 36      # The HOME key.
    Left               = 37      # The LEFT ARROW key.
    Up                 = 38      # The UP ARROW key.
    Right              = 39      # The RIGHT ARROW key.
    Down               = 40      # The DOWN ARROW key.
    Select             = 41      # The SELECT key.
    Print              = 42      # The PRINT key.
    Execute            = 43      # The EXECUTE key.
    PrintScreen        = 44      # The PRINT SCREEN key.
    Insert             = 45      # The INS key.
    Delete             = 46      # The DEL key.
    Help               = 47      # The HELP key.
    Zero               = 48      # The 0 key.
    One                = 49      # The 1 key.
    Two                = 50      # The 2 key.
    Three              = 51      # The 3 key.
    Four               = 52      # The 4 key.
    Five               = 53      # The 5 key.
    Six                = 54      # The 6 key.
    Seven              = 55      # The 7 key.
    Eight              = 56      # The 8 key.
    Nine               = 57      # The 9 key.
    A                  = 65      # The A key.
    B                  = 66      # The B key.
    C                  = 67      # The C key.
    D                  = 68      # The D key.
    E                  = 69      # The E key.
    F                  = 70      # The F key.
    G                  = 71      # The G key.
    H                  = 72      # The H key.
    I                  = 73      # The I key.
    J                  = 74      # The J key.
    K                  = 75      # The K key.
    L                  = 76      # The L key.
    M                  = 77      # The M key.
    N                  = 78      # The N key.
    O                  = 79      # The O key.
    P                  = 80      # The P key.
    Q                  = 81      # The Q key.
    R                  = 82      # The R key.
    S                  = 83      # The S key.
    T                  = 84      # The T key.
    U                  = 85      # The U key.
    V                  = 86      # The V key.
    W                  = 87      # The W key.
    X                  = 88      # The X key.
    Y                  = 89      # The Y key.
    Z                  = 90      # The Z key.
    LeftWin            = 91      # The left Windows logo key (Microsoft Natural Keyboard).
    RightWin           = 92      # The right Windows logo key (Microsoft Natural Keyboard).
    Apps               = 93      # The application key (Microsoft Natural Keyboard).
    Sleep              = 95      # The computer sleep key.
    NumPad0            = 96      # The 0 key on the numeric keypad.
    NumPad1            = 97      # The 1 key on the numeric keypad.
    NumPad2            = 98      # The 2 key on the numeric keypad.
    NumPad3            = 99      # The 3 key on the numeric keypad.
    NumPad4            = 100     # The 4 key on the numeric keypad.
    NumPad5            = 101     # The 5 key on the numeric keypad.
    NumPad6            = 102     # The 6 key on the numeric keypad.
    NumPad7            = 103     # The 7 key on the numeric keypad.
    NumPad8            = 104     # The 8 key on the numeric keypad.
    NumPad9            = 105     # The 9 key on the numeric keypad.
    Multiply           = 106     # The multiply key.
    Add                = 107     # The add key.
    Separator          = 108     # The separator key.
    Subtract           = 109     # The subtract key.
    Decimal            = 110     # The decimal key.
    Divide             = 111     # The divide key.
    F1                 = 112     # The F1 key.
    F2                 = 113     # The F2 key.
    F3                 = 114     # The F3 key.
    F4                 = 115     # The F4 key.
    F5                 = 116     # The F5 key.
    F6                 = 117     # The F6 key.
    F7                 = 118     # The F7 key.
    F8                 = 119     # The F8 key.
    F9                 = 120     # The F9 key.
    F10                = 121     # The F10 key.
    F11                = 122     # The F11 key.
    F12                = 123     # The F12 key.
    F13                = 124     # The F13 key.
    F14                = 125     # The F14 key.
    F15                = 126     # The F15 key.
    F16                = 127     # The F16 key.
    F17                = 128     # The F17 key.
    F18                = 129     # The F18 key.
    F19                = 130     # The F19 key.
    F20                = 131     # The F20 key.
    F21                = 132     # The F21 key.
    F22                = 133     # The F22 key.
    F23                = 134     # The F23 key.
    F24                = 135     # The F24 key.
    NumLock            = 144     # The NUM LOCK key.
    Scroll             = 145     # The SCROLL LOCK key.
    LeftShift          = 160     # The left SHIFT key.
    RightShift         = 161     # The right SHIFT key.
    LeftCtrl           = 162     # The left CTRL key.
    RightCtrl          = 163     # The right CTRL key.
    LeftAlt            = 164     # The left ALT key.
    RightAlt           = 165     # The right ALT key.
    BrowserBack        = 166     # The browser back key.
    BrowserForward     = 167     # The browser forward key.
    BrowserRefresh     = 168     # The browser refresh key.
    BrowserStop        = 169     # The browser stop key.
    BrowserSearch      = 170     # The browser search key.
    BrowserFavorites   = 171     # The browser favorites key.
    BrowserHome        = 172     # The browser home key.
    VolumeMute         = 173     # The volume mute key.
    VolumeDown         = 174     # The volume down key.
    VolumeUp           = 175     # The volume up key.
    MediaNextTrack     = 176     # The media next track key.
    MediaPreviousTrack = 177     # The media previous track key.
    MediaStop          = 178     # The media Stop key.
    MediaPlayPause     = 179     # The media play pause key.
    LaunchMail         = 180     # The launch mail key.
    SelectMedia        = 181     # The select media key.
    LaunchApplication1 = 182     # The start application one key.
    LaunchApplication2 = 183     # The start application two key.
    OemSemicolon       = 186     # The OEM Semicolon key on a US standard keyboard.
    Oem1               = 186     # The OEM 1 key.
    OemPlus            = 187     # The OEM plus key on any country/region keyboard.
    OemComma           = 188     # The OEM comma key on any country/region keyboard.
    OemMinus           = 189     # The OEM minus key on any country/region keyboard.
    OemPeriod          = 190     # The OEM period key on any country/region keyboard.
    OemQuestion        = 191     # The OEM question mark key on a US standard keyboard.
    Oem2               = 191     # The OEM 2 key.
    OemTilde           = 192     # The OEM tilde key on a US standard keyboard.
    Oem3               = 192     # The OEM 3 key.
    Ñ                  = 192     # The Ñ key.
    OemOpenBrackets    = 219     # The OEM open bracket key on a US standard keyboard.
    Oem4               = 219     # The OEM 4 key.
    OemPipe            = 220     # The OEM pipe key on a US standard keyboard.
    Oem5               = 220     # The OEM 5 key.
    OemCloseBrackets   = 221     # The OEM close bracket key on a US standard keyboard.
    Oem6               = 221     # The OEM 6 key.
    OemQuotes          = 222     # The OEM singled/double quote key on a US standard keyboard.
    Oem7               = 222     # The OEM 7 key.
    Oem8               = 223     # The OEM 8 key.
    OemBackslash       = 226     # The OEM angle bracket or backslash key on the RT 102 key keyboard.
    Oem102             = 226     # The OEM 102 key.
    ProcessKey         = 229     # The PROCESS KEY key.
    Packet             = 231     # Used to pass Unicode characters as if they were keystrokes. The Packet key value is the low word of a 32-bit virtual-key value used for non-keyboard input methods.
    Attn               = 246     # The ATTN key.
    Crsel              = 247     # The CRSEL key.
    Exsel              = 248     # The EXSEL key.
    EraseEof           = 249     # The ERASE EOF key.
    Play               = 250     # The PLAY key.
    Zoom               = 251     # The ZOOM key.
    NoName             = 252     # A constant reserved for future use.
    Pa1                = 253     # The PA1 key.
    OemClear           = 254     # The CLEAR key.
    KeyCode            = 65535   # The bitmask to extract a key code from a key value.
    Shift              = 65536   # The SHIFT modifier key.
    Control            = 131072  # The CTRL modifier key.
    Alt                = 262144  # The ALT modifier key.

class MouseState(IntEnum):
    Move             = 0x0000  # Estado del mouse: movimiento.
    LeftButtonDown   = 0x0001  # Estado del mouse: botón izquierdo hacia abajo (#1).
    LeftButtonUp     = 0x0002  # Estado del mouse: botón izquierdo hacia arriba (#1).
    RightButtonDown  = 0x0004  # Estado del mouse: botón derecho hacia abajo (#2).
    RightButtonUp    = 0x0008  # Estado del mouse: botón derecho hacia arriba (#2).
    MuddleButtonDown = 0x0010  # Estado del mouse: botón medio hacia abajo (#3).
    MiddleButtonUp   = 0x0020  # Estado del mouse: botón medio hacia arriba (#3).
    XButton1Down     = 0x0040  # Estado del mouse: botón X1 hacia abajo (#4).
    XButton1Up       = 0x0080  # Estado del mouse: botón X1 hacia arriba (#4).
    XButton2Down     = 0x0100  # Estado del mouse: botón X2 hacia abajo (#5).
    XButton2Up       = 0x0200  # Estado del mouse: botón X2 hacia arriba (#5).
    VerticalWheel    = 0x0400  # Estado del mouse: rueda vertical.
    HorizontalWheel  = 0x0800  # Estado del mouse: rueda horizontal.

class KeyState(IntEnum):
    Down            = 0x0000  # Estado del teclado: tecla hacia abajo.
    Up              = 0x0001  # Estado del teclado: tecla hacia arriba.
    E0Down          = 0x0002  # Estado del teclado: E0 hacia abajo.
    E0Up            = 0x0003  # Estado del teclado: E0 hacia arriba.
    E1Down          = 0x0004  # Estado del teclado: E1 hacia abajo.
    E1Up            = 0x0005  # Estado del teclado: E1 hacia arriba.
    TermSrvSetLed   = 0x0008  # Estado del teclado: TERMSRV_SET_LED.
    TermSrvShadow   = 0x0010  # Estado del teclado: TERMSRV_SHADOW.
    TermSrvVkPacked = 0x0020  # Estado del teclado: TERMSRV_VKPACKET.

class MouseFilter(IntFlag):
    All              = 0xFFFF  # Filtro del mouse: todos los botones, rueda y movimiento.
    ButtonAll        = 0x03FF  # Filtro del mouse: todos los botones.
    ButtonDownAll    = 0x0155  # Filtro del mouse: todos los botones hacia abajo.
    ButtonUpAll      = 0x02AA  # Filtro del mouse: todos los botones hacia arriba.
    WheelAll         = 0x0C00  # Filtro del mouse: rueda horizontal y vertical.
    LeftButtonDown   = 0x0001  # Filtro del mouse: botón izquierdo hacia abajo.
    LeftButtonUp     = 0x0002  # Filtro del mouse: boton izquierdo hacia arriba.
    RightButtonDown  = 0x0004  # Filtro del mouse: botón derecho hacia abajo.
    RightButtonUp    = 0x0008  # Filtro del mouse: botón derecho hacia arriba.
    MiddleButtonDown = 0x0010  # Filtro del mouse: botón central hacia abajo.
    MiddleButtonUp   = 0x0020  # Filtro del mouse: botón central hacia arriba.
    XButton1Down     = 0x0040  # Filtro del mouse: botón X1 hacia abajo.
    XButton1Up       = 0x0080  # Filtro del mouse: botón X1 hacia arriba.
    XButton2Down     = 0x0100  # Filtro del mouse: botón X2 hacia abajo.
    XButton2Up       = 0x0200  # Filtro del mouse: botón X2 hacia arriba.
    VerticalWheel    = 0x0400  # Filtro del mouse: rueda vertical.
    HorizontalWheel  = 0x0800  # Filtro del mouse: rueda horizontal.
    Move             = 0x1000  # Filtro del mouse: movimiento.

class KeyFilter(IntFlag):
    All             = 0xFFFF  # Filtro del teclado: todas las teclas.
    Down            = 0x0001  # Filtro del teclado: teclas hacia abajo.
    Up              = 0x0002  # Filtro del teclado: teclas hacia arriba.
    E0              = 0x0004  # Filtro del teclado: E0.
    E1              = 0x0008  # Filtro del teclado: E1.
    TermSrvSetLed   = 0x0010  # Filtro del teclado: TERMSRV_SET_LED.
    TermSrvShadow   = 0x0020  # Filtro del teclado: TERMSRV_SHADOW.
    TermSrvVkPacket = 0x0040  # Filtro del teclado: TERMSRV_VKPACKET.

class MouseFlags(IntEnum):
    MoveRelative      = 0x000  # Mouse Flags: coordenadas relativas.
    MoveAbsolute      = 0x001  # Mouse Flags: coordenadas absolutas.
    VirtualDesktop    = 0x002  # Mouse Flags: coordenadas del escritorio virtual.
    AttributesChanged = 0x004  # Mouse Flags: ATTRIBUTES_CHANGED.
    MoveNoCoalesce    = 0x008  # Mouse Flags: MOVE_NOCOALESCE.
    TermSrvSrcShadow  = 0x100  # Mouse Flags: TERMSRV_SRC_SHADOW.

class KeyStroke(Structure):
    _fields_ = [
        ('id', USHORT), # *UnitId
        ('code', USHORT), # MakeCode
        ('state', USHORT), # Flags
        ('reserved', USHORT), # *Reserved
        ('info', ULONG) # ExtraInformation
    ]

class MouseStroke(Structure):
    _fields_ = [
        ('id', USHORT), # *UnitId
        ('flags', USHORT), # Flags
        ('state', USHORT), # ButtonFlags
        ('rolling', SHORT), # ButtonData
        ('rawbtns', ULONG), # *RawButtons
        ('x', LONG), # LastX
        ('y', LONG), # LastY
        ('info', ULONG) # ExtraInformation
    ]

def is_device(x:int):
    return MIN_DEVICE <= x <= MAX_DEVICE

def is_keyboard(x:int):
    return MIN_KEYBOARD <= x <= MAX_KEYBOARD

def is_mouse(x:int):
    return MIN_MOUSE <= x <= MAX_MOUSE

def win_function(dll, name, restype, *args, **kwargs):
    argtypes, argflags = [], []
    for arg in args:
        arg = [*arg]
        argtypes.append(arg.pop(0))
        argflags.append((1,) + tuple(arg))
    prototype = WINFUNCTYPE(restype, *argtypes)
    func = prototype((name, dll), tuple(argflags))
    if 'errcheck' in kwargs:
        func.errcheck = kwargs['errcheck']
    return func

# noinspection PyUnusedLocal
def errcheck_bool(result, func, args):
    if not result:
        raise WinError()
    return result

# noinspection PyUnusedLocal
def errcheck_wait_failed(result, func, args):
    if result == WAIT_FAILED:
        raise WinError()
    return result

close_handle = win_function(windll.kernel32, 'CloseHandle', BOOL,
    (HANDLE,'handle'), errcheck=errcheck_bool)

class Handle:
    def __init__(self, handle):
        self.handle = handle

    def __del__(self):
        if self.handle:
            close_handle(self.handle)

    def close(self):
        close_handle(self.handle)
        self.handle = 0

# noinspection PyUnusedLocal
def errcheck_handle(result, func, args):
    if not result or result == INVALID_HANDLE_VALUE:
        raise WinError()
    return Handle(result)

create_file = win_function(windll.kernel32, 'CreateFileW', HANDLE,
    (LPCWSTR,'filename'), (DWORD,'access',0), (DWORD,'share_mode',0), (LPVOID,'secutiry_attr',None),
    (DWORD,'creation_disp',3), (DWORD,'flags',0), (HANDLE,'template_file',None),
    errcheck=errcheck_handle)

create_event = win_function(windll.kernel32, 'CreateEventW', HANDLE,
    (LPVOID,'event_attr',None), (BOOL,'manual_reset',False), (BOOL,'initial_state',False), (LPCWSTR,'name',None),
    errcheck=errcheck_handle)

def device_io_control(handle, code, inbuff=None, outbuff=None):
    bytes_returned = DWORD()
    if inbuff is None: inbuffer_p, insize = None, 0
    else: inbuffer_p, insize = cast(byref(inbuff),LPVOID), sizeof(inbuff)
    if outbuff is None: outbuffer_p, outsize = None, 0
    else: outbuffer_p, outsize = cast(byref(outbuff),LPVOID), sizeof(outbuff)
    device_io_control.func(handle, code, inbuffer_p, insize, outbuffer_p, outsize, bytes_returned)
    return bytes_returned.value
device_io_control.func = win_function(windll.kernel32, 'DeviceIoControl', BOOL,
    (HANDLE,'device'), (DWORD,'code'), (LPVOID,'inbuff',None), (DWORD,'insize',0), (LPVOID,'outbuff',None),
    (DWORD,'outsize',0), (LPDWORD,'outbytes',None), (LPVOID,'overlapped',None),
    errcheck=errcheck_bool)

def wait_for_multiple_objects(handles, wait_all=False, milliseconds=INFINITE) -> int:
    return wait_for_multiple_objects.func(len(handles), handles, wait_all, milliseconds)
wait_for_multiple_objects.func = win_function(windll.kernel32, 'WaitForMultipleObjects', DWORD,
    (DWORD,'count'), (PHANDLE,'handles'), (BOOL,'wait_all',False), (DWORD,'milliseconds',INFINITE),
    errcheck=errcheck_wait_failed)

map_virtual_key = win_function(windll.user32, 'MapVirtualKeyW', UINT, (UINT,'code'), (UINT,'type'))
get_key_state = win_function(windll.user32, 'GetKeyState', SHORT, (INT,'vk'))
get_async_key_state = win_function(windll.user32, 'GetAsyncKeyState', SHORT, (INT,'vk'))

def is_key_pressed(vk, async_=True):
    if async_:
        return (get_async_key_state(vk) & 0x8000) == 0x8000
    return (get_key_state(vk) & 0x8000) == 0x8000

def is_key_toggled(vk):
    return (get_key_state(vk) & 0x0001) == 0x0001

class Device:
    def __init__(self, device:int):
        self.device = create_file(fr'\\.\interception{device-1:02}', 0x80000000)
        self.event = create_event(manual_reset=True)
        self.is_mouse = is_mouse(device)
        self.is_keyboard = is_keyboard(device)
        self.stroke = MouseStroke() if self.is_mouse else KeyStroke()

        zero_padded_handle = (HANDLE * 2)(self.event.handle)
        device_io_control(self.device.handle, IOCTL_SET_EVENT, zero_padded_handle)

    def __del__(self):
        if hasattr(self, 'device'): self.device.close()
        if hasattr(self, 'event'): self.event.close()

    def receive(self):
        device_io_control(self.device.handle, IOCTL_READ, None, self.stroke)

    def send(self, stroke=None):
        device_io_control(self.device.handle, IOCTL_WRITE, stroke or self.stroke)

    def get_filter(self):
        filter = USHORT()
        device_io_control(self.device.handle, IOCTL_GET_FILTER, None, filter)
        return MouseFilter(filter.value) if self.is_mouse else KeyFilter(filter.value)

    def set_filer(self, filter):
        device_io_control(self.device.handle, IOCTL_SET_FILTER, USHORT(int(filter)))

    def get_precedence(self):
        precedence = INT()
        device_io_control(self.device.handle, IOCTL_GET_PRECEDENCE, None, precedence)
        return precedence.value

    def set_precedence(self, precedence:int):
        device_io_control(self.device.handle, IOCTL_SET_PRECEDENCE, INT(precedence))

    def get_hardware_id(self):
        hardware_id = create_unicode_buffer(250)
        if device_io_control(self.device.handle, IOCTL_GET_HARDWARE_ID, None, hardware_id):
            return hardware_id.value

class Interception:
    _context: list[Device] = []
    _events = (HANDLE * MAX_DEVICE)()

    def __init__(self):
        for i in range(MAX_DEVICE):
            device = Device(i+1)
            self._context.append(device)
            self._events[i] = device.event.handle

    def set_filter(self, predicate, filter):
        for i in range(MAX_DEVICE):
            if predicate(i+1):
                self._context[i].set_filer(filter)

    def set_mouse_filter(self, filter):
        self.set_filter(is_mouse, filter)

    def set_keyboard_filter(self, filter):
        self.set_filter(is_keyboard, filter)

    def wait(self, milliseconds=INFINITE):
        ret = wait_for_multiple_objects(self._events, milliseconds=milliseconds)
        return None if ret == WAIT_TIMEOUT else self._context[ret]

    def wait_receive(self, milliseconds=INFINITE):
        device = self.wait(milliseconds)
        if device:
            device.receive()
        return device
