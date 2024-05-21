
def create_visuals(do_DOF, do_120, do_docked):

    fps120 = "disabled"
    docked = "disabled"
    dof = "disabled"

    
    visual_fixes = []

    if do_DOF:
        dof = "enabled"
    if do_120:
        fps120 = "enabled"
    if do_docked:
        docked = "enabled"
        
    visuals1_0_0 = f'''// 2560x1440 Docked
@{docked}
044C35A0 C960A852
08982f10 1F2003D5
@disabled

// 120 FPS
@{fps120}
0895DCDE 1F2003D5
01E556B4 E8008052
01E556BC 084EA852

// Disable DOF
@{dof}
0894782c 1F2003D5
02715b14 02008052
@stop
'''


    visual_fixes.append(visuals1_0_0)
    
    return visual_fixes