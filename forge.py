#!/usr/bin/env python3
import os
import sys
import time
import random
import math
import string
import subprocess
import select

try:
    import pyfiglet
    import questionary
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.live import Live
    from rich.markdown import Markdown
except ImportError:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[91m" + "═" * 50 + "\033[0m")
    print("\033[91m║\033[0m \033[1;93m⚠️  MISSING CORE DEPENDENCIES!\033[0m" + " " * 18 + "\033[91m║\033[0m")
    print("\033[91m║\033[0m Please install the required lightweight libraries: \033[91m║\033[0m")
    print("\033[91m║\033[0m \033[1;97mpip install -r requirements.txt\033[0m                    \033[91m║\033[0m")
    print("\033[91m" + "═" * 50 + "\033[0m")
    sys.exit(1)

if os.name != 'nt':
    import tty
    import termios

console = Console()

def clear_screen():
    console.clear()

def show_header():
    console.clear()
    banner = pyfiglet.figlet_format("FORGE", font="slant")
    console.print(f"[cyan]{banner}[/cyan]")
    console.print(Panel("[bold green]🗡️ The Swiss Army Knife Terminal 🗡️[/bold green]", expand=False))

def matrix_rain():
    clear_screen()
    cols, rows = os.get_terminal_size()
    drops = [0 for _ in range(cols)]
    
    try:
        while True:
            out = ""
            for i in range(cols):
                if random.random() > 0.95:
                    drops[i] = 0
                
                if drops[i] < rows:
                    char = chr(random.randint(0x30A0, 0x30FF))
                    out += f"\033[{drops[i]};{i}H\033[97m{char}\033[0m"
                    if drops[i] > 0:
                        char2 = chr(random.randint(0x30A0, 0x30FF))
                        out += f"\033[{drops[i]-1};{i}H\033[92m{char2}\033[0m"
                    if drops[i] > 1:
                        char3 = chr(random.randint(0x30A0, 0x30FF))
                        out += f"\033[{drops[i]-2};{i}H\033[32m{char3}\033[0m"
                    
                    drops[i] += 1
            
            print(out, end="", flush=True)
            time.sleep(0.05)
    except KeyboardInterrupt:
        return

def spirograph():
    clear_screen()
    cols, rows = os.get_terminal_size()
    R, r, d = 20, 5, 10
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    
    theta = 0.0
    try:
        while True:
            clear_screen()
            out = ""
            for t_step in range(0, int(theta), 1):
                t = t_step * 0.1
                x = (R - r) * math.cos(t) + d * math.cos(((R - r) / r) * t)
                y = (R - r) * math.sin(t) - d * math.sin(((R - r) / r) * t)
                
                grid_x = int(cols / 2 + x * 2)
                grid_y = int(rows / 2 + y)
                
                if 0 <= grid_x < cols and 0 <= grid_y < rows:
                    color = colors[t_step % len(colors)]
                    out += f"\033[{grid_y};{grid_x}H[{color}]*[/{color}]"
            
            console.print(out, end="")
            theta += 1.0
            time.sleep(0.03)
    except KeyboardInterrupt:
        return

def _getch():
    if os.name == 'nt':
        import msvcrt
        return msvcrt.getch().decode('utf-8')
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def _non_blocking_getch():
    if os.name == 'nt':
        import msvcrt
        if msvcrt.kbhit():
            return msvcrt.getch()
        return None
    else:
        dr, dw, de = select.select([sys.stdin], [], [], 0)
        if dr:
            return sys.stdin.read(1)
        return None

def hacker_typer():
    quotes = [
        "Talk is cheap. Show me the code. - Linus Torvalds",
        "Programs must be written for people to read, and only incidentally for machines to execute. - Harold Abelson",
        "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. - Martin Fowler",
        "First, solve the problem. Then, write the code. - John Johnson",
        "Experience is the name everyone gives to their mistakes. - Oscar Wilde"
    ]
    quote = random.choice(quotes)
    
    typed = ""
    start_time = None
    
    while True:
        clear_screen()
        console.print(Panel("[bold cyan]Hacker Typer[/bold cyan]\nType the quote below as fast as you can. No backspace!", expand=False))
        
        display_quote = ""
        errors = 0
        for i, c in enumerate(quote):
            if i < len(typed):
                if typed[i] == c:
                    display_quote += f"[green]{typed[i]}[/green]"
                else:
                    display_quote += f"[red]{typed[i]}[/red]"
                    errors += 1
            else:
                display_quote += f"[dim]{c}[/dim]"
        
        console.print(display_quote)
        
        if len(typed) > 0 and start_time:
            elapsed = time.time() - start_time
            wpm = (len(typed) / 5) / (elapsed / 60) if elapsed > 0 else 0
            acc = max(0, ((len(typed) - errors) / len(typed)) * 100) if len(typed) > 0 else 100
            console.print(f"\n[cyan]WPM: {wpm:.1f} | ACC: {acc:.1f}% | Time: {elapsed:.1f}s[/cyan]")
        
        if len(typed) == len(quote):
            break
            
        try:
            ch = _getch()
            if ord(ch) == 3: # Ctrl+C
                return
            if start_time is None:
                start_time = time.time()
            typed += ch
        except KeyboardInterrupt:
            return
            
    console.print("\n[bold green]Finished! Press Enter to return to menu...[/bold green]")
    _getch() # Wait for keypress

def qr_generator():
    try:
        import qrcode
    except ImportError:
        console.print(Panel("⚠️ QR Generator requires 'qrcode'.\nInstall with: [bold white]pip install qrcode[/bold white]", style="bold red", expand=False))
        console.input("\nPress Enter to continue...")
        return
        
    clear_screen()
    text = questionary.text("Enter text or URL to encode:").ask()
    if not text:
        return
        
    qr = qrcode.QRCode(version=1, box_size=1, border=1)
    qr.add_data(text)
    qr.make(fit=True)
    matrix = qr.get_matrix()
    
    out = ""
    for row in matrix:
        for val in row:
            out += "██" if val else "  "
        out += "\n"
        
    console.print(Panel(out, title="[bold cyan]SCAN ME[/bold cyan]", border_style="cyan", expand=False))
    console.input("\nPress Enter to continue...")

def image_to_ascii():
    try:
        from PIL import Image
    except ImportError:
        console.print(Panel("⚠️ Image Preview requires 'pillow'.\nInstall with: [bold white]pip install pillow[/bold white]", style="bold red", expand=False))
        console.input("\nPress Enter to continue...")
        return
        
    clear_screen()
    path = questionary.path("Enter image file path:").ask()
    if not path or not os.path.exists(path):
        console.print("[red]Invalid path[/red]")
        time.sleep(1)
        return
        
    try:
        img = Image.open(path).convert('L')
        cols, _ = os.get_terminal_size()
        width = min(80, cols - 4)
        
        aspect_ratio = img.height / img.width
        new_height = int(aspect_ratio * width * 0.45)
        img = img.resize((width, new_height))
        
        chars = ["█", "▓", "▒", "░", " "]
        pixels = img.getdata()
        
        out = ""
        for i, p in enumerate(pixels):
            if i > 0 and i % width == 0:
                out += "\n"
            out += chars[int(p / 256 * len(chars))]
            
        console.print(Panel(out, border_style="green", expand=False))
        console.input("\nPress Enter to continue...")
    except Exception as e:
        console.print(f"[red]Error processing image: {e}[/red]")
        time.sleep(2)

def video_player():
    try:
        import imageio
        import numpy as np
        from PIL import Image
    except ImportError:
        console.print(Panel(
            "⚠️ Video Player requires 'imageio', 'imageio-ffmpeg', 'numpy', and 'pillow'.\n"
            "Install with: [bold white]pip install imageio imageio-ffmpeg numpy pillow[/bold white]",
            style="bold red", expand=False
        ))
        console.input("\nPress Enter to continue...")
        return
        
    clear_screen()
    path = questionary.path("Enter mp4 file path:").ask()
    if not path or not os.path.exists(path):
        console.print("[red]Invalid path[/red]")
        time.sleep(1)
        return
        
    try:
        reader = imageio.get_reader(path)
        meta = reader.get_meta_data()
        fps = meta.get('fps', 30)
        total_frames = meta.get('nframes', 0)
    except Exception as e:
        console.print(f"[red]Failed to open video: {e}[/red]")
        time.sleep(2)
        return
        
    chars = ["█", "▓", "▒", "░", " "]
    paused = False
    
    if os.name != 'nt':
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setraw(sys.stdin.fileno())
        
    try:
        current_frame_idx = 0
        while True:
            ch = _non_blocking_getch()
            if ch:
                if ch == 'q' or ch == b'q':
                    break
                elif ch == ' ' or ch == b' ':
                    paused = not paused
                elif ch == '\x1b': # Escape sequence for arrows
                    ch2 = sys.stdin.read(2)
                    if ch2 == '[C': # Right arrow
                        current_frame_idx = min(total_frames - 1, current_frame_idx + int(10 * fps))
                    elif ch2 == '[D': # Left arrow
                        current_frame_idx = max(0, current_frame_idx - int(10 * fps))
            
            if paused:
                time.sleep(0.1)
                continue
                
            try:
                frame = reader.get_data(current_frame_idx)
            except IndexError:
                break
                
            frame_img = Image.fromarray(frame).convert('L')
            cols, rows = os.get_terminal_size()
            width = min(80, cols)
            
            aspect_ratio = frame_img.height / frame_img.width
            new_height = int(aspect_ratio * width * 0.45)
            frame_img = frame_img.resize((width, new_height))
            
            pixels = frame_img.getdata()
            out = ""
            for i, p in enumerate(pixels):
                if i > 0 and i % width == 0:
                    out += "\n"
                out += chars[int(p / 256 * len(chars))]
                
            curr_sec = int(current_frame_idx / fps) if fps else 0
            tot_sec = int(total_frames / fps) if total_frames > 0 and fps else 0
            
            curr_str = f"{curr_sec//60:02d}:{curr_sec%60:02d}"
            tot_str = f"{tot_sec//60:02d}:{tot_sec%60:02d}"
            
            prog_len = 12
            prog_filled = int((current_frame_idx / total_frames) * prog_len) if total_frames > 0 else 0
            prog_bar = "█" * prog_filled + "░" * (prog_len - prog_filled)
            status_icon = "⏸️" if paused else "▶️"
            
            status_bar = f"\n{status_icon} [{prog_bar}] {curr_str} / {tot_str} | Space: Pause | L/R: Skip | q: Quit"
            
            sys.stdout.write('\033[H')
            sys.stdout.write(out + status_bar)
            sys.stdout.flush()
            
            current_frame_idx += 1
            time.sleep(1/fps)
    except Exception:
        pass
    finally:
        if os.name != 'nt':
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        reader.close()

def iron_vault():
    clear_screen()
    length = questionary.text("Enter password length:", default="16").ask()
    try:
        length = int(length)
    except (ValueError, TypeError):
        length = 16
        
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    pwd = "".join(random.choice(chars) for _ in range(length))
    
    score = min(5, length // 4)
    if any(c in "!@#$%^&*()" for c in pwd):
        score += 1
    score = min(5, score)
    
    labels = ["Weak", "Weak", "Moderate", "Strong", "Strong", "Fort Knox"]
    label = labels[score]
    bar = "█" * score + "░" * (5 - score)
    
    console.print(Panel(f"[bold cyan]{pwd}[/bold cyan]\n\nStrength: {bar} ({label})", title="[bold yellow]Iron Vault[/bold yellow]", expand=False))
    
    try:
        if os.name == 'nt':
            subprocess.run(['clip'], input=pwd.encode(), check=True)
        elif sys.platform == 'darwin':
            subprocess.run(['pbcopy'], input=pwd.encode(), check=True)
        else:
            subprocess.run(['xclip', '-selection', 'clipboard'], input=pwd.encode(), check=True)
        console.print("[green]Password copied to clipboard![/green]")
    except Exception:
        pass
        
    console.input("\nPress Enter to return to menu...")

def file_locker():
    try:
        from cryptography.fernet import Fernet
    except ImportError:
        console.print(Panel("⚠️ File Locker requires 'cryptography'.\nInstall with: [bold white]pip install cryptography[/bold white]", style="bold red", expand=False))
        console.input("\nPress Enter to continue...")
        return
        
    clear_screen()
    action = questionary.select("Choose action:", choices=["Encrypt File", "Decrypt File"]).ask()
    if not action: return
    
    path = questionary.path("Enter file path:").ask()
    if not path or not os.path.exists(path):
        console.print("[red]File not found.[/red]")
        time.sleep(1)
        return

    try:
        if action == "Encrypt File":
            key = Fernet.generate_key()
            f = Fernet(key)
            with open(path, 'rb') as file:
                original = file.read()
            encrypted = f.encrypt(original)
            out_path = path + '.locked'
            with open(out_path, 'wb') as file:
                file.write(encrypted)
            console.print(Panel(f"File encrypted to: [bold green]{out_path}[/bold green]\n\nYOUR KEY (SAVE THIS!):\n[bold yellow]{key.decode()}[/bold yellow]", title="File Locked 🔐", expand=False))
        else:
            key = questionary.password("Enter decryption key:").ask()
            if not key: return
            f = Fernet(key.encode())
            with open(path, 'rb') as file:
                encrypted = file.read()
            decrypted = f.decrypt(encrypted)
            out_path = path.replace('.locked', '') if '.locked' in path else path + '.unlocked'
            with open(out_path, 'wb') as file:
                file.write(decrypted)
            console.print(Panel(f"File decrypted to: [bold green]{out_path}[/bold green]", title="File Unlocked 🔓", expand=False))
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
        
    console.input("\nPress Enter to return to menu...")

def system_scope():
    try:
        import psutil
    except ImportError:
        console.print(Panel(
            "⚠️ System Scope requires 'psutil'.\n"
            "Install with: [bold white]pip install psutil[/bold white]\n\n"
            "(Note: psutil may not compile properly on Android/Termux environments)",
            style="bold red", expand=False
        ))
        console.input("\nPress Enter to continue...")
        return
        
    try:
        with Live(refresh_per_second=1) as live:
            while True:
                cpu = psutil.cpu_percent()
                mem = psutil.virtual_memory().percent
                disk = psutil.disk_usage('/').percent
                
                table = Table(title="📊 System Scope", show_header=True, header_style="bold magenta")
                table.add_column("Metric", style="cyan")
                table.add_column("Usage", justify="right")
                table.add_column("Bar", justify="left")
                
                def make_bar(pct):
                    filled = int((pct / 100) * 20)
                    color = "green" if pct < 70 else "yellow" if pct < 90 else "red"
                    return f"[{color}]{'█' * filled}{'░' * (20 - filled)}[/{color}]"
                    
                table.add_row("CPU", f"{cpu}%", make_bar(cpu))
                table.add_row("RAM", f"{mem}%", make_bar(mem))
                table.add_row("DISK", f"{disk}%", make_bar(disk))
                
                live.update(table)
                time.sleep(1)
    except KeyboardInterrupt:
        return

def main():
    while True:
        show_header()
        choice = questionary.select(
            "Choose an option:",
            choices=[
                "🌧️ Matrix Digital Rain",
                "🌀 Hypnotic Spirograph",
                "⌨️ Hacker Typer",
                "📱 ASCII QR Generator",
                "🖼️ Image to ASCII Preview",
                "🎬 Video Player (ASCII Cinema)",
                "🔐 Iron Vault (Password Gen)",
                "🗄️ File Locker (Cryptography)",
                "📊 System Scope",
                "❌ Exit Forge"
            ],
            pointer="👉 "
        ).ask()
        
        if not choice or choice.startswith("❌"):
            break
            
        if choice.startswith("🌧️"):
            matrix_rain()
        elif choice.startswith("🌀"):
            spirograph()
        elif choice.startswith("⌨️"):
            hacker_typer()
        elif choice.startswith("📱"):
            qr_generator()
        elif choice.startswith("🖼️"):
            image_to_ascii()
        elif choice.startswith("🎬"):
            video_player()
        elif choice.startswith("🔐"):
            iron_vault()
        elif choice.startswith("🗄️"):
            file_locker()
        elif choice.startswith("📊"):
            system_scope()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        sys.exit(0)
