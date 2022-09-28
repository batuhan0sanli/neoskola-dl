import sys
import time
import pyautogui
import pyperclip


def get_course_info(driver):
    # config for operating system
    cmd_ctrl = 'command' if sys.platform == 'darwin' else 'ctrl'
    console_panel = ('command', 'option', 'j') if sys.platform == 'darwin' else ('ctrl', 'shift', 'j')

    # open console panel
    pyautogui.press('f12')
    time.sleep(1)
    pyautogui.hotkey(*console_panel)
    time.sleep(1)

    # select course div
    select_text = 'inspect(document.getElementById("course-view-div"));'
    pyperclip.copy(select_text)
    pyautogui.hotkey(cmd_ctrl, 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    # go to react components tab
    for _ in range(2):
        time.sleep(0.1)
        pyautogui.hotkey(cmd_ctrl, '[')
    time.sleep(1)

    # get course info
    course_info = driver.driver.execute_script('return $r.props.children.props.value;')
    return course_info
