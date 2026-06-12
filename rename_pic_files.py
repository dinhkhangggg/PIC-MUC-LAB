import os
import re
import codecs

rename_map = {
    "2nutrunstop1den300": "Two_Buttons_Run_Stop_LED_Delay",
    "2nutsangtat": "Two_Buttons_On_Off",
    "32ledsangvaotrong": "32_LEDs_Inward_Effect",
    "74595_32LED": "74595_32_LEDs",
    "74595_8L7D_MBI": "74595_8_LED_7_Segment_MBI",
    "74595_BUZZER": "74595_Buzzer",
    "Hiensotheoled_tensinhvien": "Display_Number_LED_Student_Name",
    "LEDTHU8_16BATBUZZER": "8th_16th_LED_Turn_On_Buzzer",
    "PWM1-2ms70%": "PWM1_2ms_70_Percent",
    "PWM1-POT": "PWM1_Potentiometer",
    "SangDanD1-D32": "Sequential_Turn_On_D1_To_D32",
    "YC1-TestHW": "Req1_Test_Hardware",
    "adc_canhbao": "ADC_Warning",
    "adc_nhietdocai": "ADC_Set_Temperature",
    "baicuoiky": "Final_Exam",
    "baicuoiky1led7doan": "Final_Exam_1_7_Segment_LED",
    "baicuoikydiemcaonhe": "Final_Exam_High_Score",
    "baithicuaHuy": "Huy_Exam",
    "baithicuoiky": "Final_Exam_Test",
    "baithitonghop_10072025": "Comprehensive_Exam_10072025",
    "countyc1": "Counter_Req1",
    "countyc2": "Counter_Req2",
    "countyc3": "Counter_Req3",
    "cuoikydiemcaomanifest": "Final_Exam_High_Score_Manifest",
    "d": "Misc_Test_D",
    "demnhiphantren32led_7doan": "Binary_Counter_32_LEDs_7_Segment",
    "demnhiphantren32led_demnhiphan7doan": "Binary_Counter_32_LEDs_And_7_Segment",
    "donghoAI": "AI_Clock",
    "hiensotheoled": "Display_Number_On_LED",
    "ma7doanchayden1000": "7_Segment_Counter_To_1000",
    "nutnhanled1_8": "Button_Control_LED_1_To_8",
    "random_min_max": "Random_Min_Max",
    "sangled1denled32": "Turn_On_LED_1_To_32",
    "sangled1denled32_p2": "Turn_On_LED_1_To_32_Part2",
    "selectadj_24092025": "Select_Adjust_24092025",
    "selectadj_eeprom": "Select_Adjust_EEPROM",
    "selecttungconso": "Select_Individual_Digit",
    "songaunhien": "Random_Number",
    "songaunhien_eeprom": "Random_Number_EEPROM",
    "songaunhientu_am50den_duong50": "Random_Number_Minus_50_To_Plus_50",
    "test03092025": "Test_03092025",
    "test03092025_2": "Test_03092025_Part2",
    "test03092025_3": "Test_03092025_Part3",
    "test27082025": "Test_27082025",
    "test7doan_10092025": "Test_7_Segment_10092025",
    "test7doan_2_10092025": "Test_7_Segment_2_10092025",
    "testadc_01102025": "Test_ADC_01102025",
    "testcounter0_1": "Test_Counter_0_1",
    "testcuoi": "Test_Final",
    "testdongco_03092025": "Test_Motor_03092025",
    "testnutnhan3chedo_10092025": "Test_Button_3_Modes_10092025",
    "testnutnhan_10092025": "Test_Button_10092025"
}

def update_file_contents(dir_path):
    text_exts = {".c", ".h", ".ccspjt", ".STA", ".pdsprj"}
    sorted_keys = sorted(rename_map.keys(), key=len, reverse=True)
    
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in text_exts:
                path = os.path.join(root, file)
                try:
                    with codecs.open(path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    
                    new_content = content
                    for old in sorted_keys:
                        new = rename_map[old]
                        if old == "d":
                            new_content = re.sub(r'\bd\.([a-zA-Z0-9]+)\b', lambda m: new + "." + m.group(1), new_content)
                        else:
                            new_content = new_content.replace(old, new)
                            
                    if new_content != content:
                        with codecs.open(path, "w", encoding="utf-8", errors="ignore") as f:
                            f.write(new_content)
                        print(f"Updated contents: {file}")
                except Exception as e:
                    print(f"Error reading/writing {path}: {e}")

def rename_files(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            name, ext = os.path.splitext(file)
            if name in rename_map:
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, rename_map[name] + ext)
                print(f"Renaming {old_path} -> {new_path}")
                os.rename(old_path, new_path)

if __name__ == "__main__":
    work_dir = r"C:\KhangLab\TTVXL"
    update_file_contents(work_dir)
    rename_files(work_dir)
