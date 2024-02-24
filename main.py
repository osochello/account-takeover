from scripts.display import *
from scripts.act import *
from scripts.show_users import *


def work_one():
    try:
        choose = int(input(f"1. Get All Users\n2. Account Take Over\n\nChoose option (1 or 2): "))
        if choose == 1:
            return 1
        elif choose == 2:
            return 2
        else:
            raise ValueError("Invalid choice. Please enter either 1 or 2.")
    except ValueError as e:
        print(f"Error: {e}")
        return None
        
def create_url():
    ip_entered = input("Enter IP Address For Server Hosting: ")
    ip = check_ip_reachability(ip_entered)
    get_url = generate_url(ip)
    if get_url:
        return get_url
    else:
        return None

def re_run_program(url):
    choose = input(f"1. Press (R) To restart The Program \n2. press Q to quit the program \n\nChoose option (R or Q): ")
    if choose.lower() == "r":
        run_prog(url)
    elif choose.lower() == "q":
        print("\nSee You Again ........")
    else:
         print("\nInvalid choice for program please try again ......")
         re_run_program(url)


def run_prog(url):
    if not url:
        g_url = create_url()
        if g_url:
            job = work_one()
            if job == 1:
                start_display_users(g_url)
                re_run_program(g_url)
            
            elif job == 2:
                account_take_over(g_url)
                re_run_program(g_url)
            else:
                print("invaild For Choosing Please try again ......")
                
        else:
            print("Not Generated Url")
    else:
        job = work_one()
        if job == 1:
            start_display_users(url)
            re_run_program(url)
            
        elif job == 2:
            account_take_over(url)
            re_run_program(url)
        else:
            print("invaild For Choosing Please try again ......")

if __name__ == '__main__':
    banner_display()
    run_prog("")