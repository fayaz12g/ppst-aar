import os
import math
from functions import *

def create_patch_files(patch_folder, ratio_value, scaling_factor, visual_fixes, ultra_wide_camera):

    visual_fixesa = visual_fixes[0]
    scaling_factor = float(scaling_factor)
    ratio_value = float(ratio_value)
    num = ((((1-scaling_factor)/2)+scaling_factor))
    print(f"The scaling factor is {num}.")
    hex_num = float_to_reversed_hex(num)
    version_variables = ["1.0.0"]
    for version_variable in version_variables:
        file_name = f"main-{version_variable}.pchtxt"
        file_path = os.path.join(patch_folder, file_name)

        if version_variable == "1.0.0":
            nsobidid = "928EFE2954F680557B8B3839481C97DB"
            ui_replace = "03e0ae68"
            visual_fix = visual_fixesa

        if ultra_wide_camera == True:
                line_3 = f"\n{ui_replace} 054DC13D"
        else:
             line_3 = ""
        patch_content = f'''@nsobid-{nsobidid}

@flag print_values
@flag offset_shift 0x100

@enabled
085fd530 {hex_num}0000000000000000000000
0488e838 174DC13D{line_3}
@disabled

{visual_fix}

// Generated using PPST-AAR by Fayaz (github.com/fayaz12g/PPST-aar)
// Made possible by Fl4sh_#9174'''
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as patch_file:
            patch_file.write(patch_content)
        print(f"{patch_file} file created.")
