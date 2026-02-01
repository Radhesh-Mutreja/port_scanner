import nmap
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import sys
import io


def run_original_scan():
    import nmap

    nm = nmap.PortScanner(nmap_search_path=[r"C:\Program Files (x86)\Nmap\nmap.exe"])

    target = "45.33.32.156"
    options = "-sV"

    nm.scan(target, arguments=options)

    for host in nm.all_hosts():
        print(f"Host : {host} ({nm[host].hostname()})")
        print(f"State : {nm[host].state()}")

        for protocol in nm[host].all_protocols():
            print(f"Protocol : {protocol}")
            ports = nm[host][protocol]

            for port, data in ports.items():
                print(f"Port : {port}\tState : {data['state']}")


def start_scan():
    scan_button.config(state=tk.DISABLED)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Scanning... please wait.\n\n")
    root.update_idletasks()

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        run_original_scan()
        output = sys.stdout.getvalue()
        output_box.insert(tk.END, output)
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        sys.stdout = old_stdout
        scan_button.config(state=tk.NORMAL)

def start_scan_thread():
    threading.Thread(target=start_scan, daemon=True).start()

    threading.Thread(target=start_scan).start()

root = tk.Tk()
root.title("Nmap Port Scanner")
root.geometry("700x500")

tk.Label(root, text="Target is hardcoded in code: 45.33.32.156").pack(pady=5)

scan_button = tk.Button(root, text="Run Scan", command=start_scan_thread)
scan_button.pack(pady=10)

output_box = scrolledtext.ScrolledText(root, width=80, height=25)
output_box.pack(padx=10, pady=10)

root.mainloop()
