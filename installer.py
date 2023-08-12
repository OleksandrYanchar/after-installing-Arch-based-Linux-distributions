import subprocess


def main():
    options = {
        "1": ("Update packages", "update_packages.sh"),
        "2": ("Install and configure git", "git_install.sh"),
        "3": ("Install Python", "python_install.sh"),
        "4": ("Create SSH key", "create_ssh_key.sh"),
        "5": ("Install Google Chrome", "install_chrome.sh"),
        "6": ("Install PyCharm", "install_pycharm.sh"),
        "7": ("Install VS Code", "install_vscode.sh"),
        "8": ("Install Vim", "install_vim.sh"),
        "9": ("Install Docker", "install_docker.sh"),
        "10": ("Install Docker Compose", "install_docker_compose.sh"),
        "11": ("Install PostgreSQL", "install_postgresql.sh"),
        "12": ("Install GCC", "gcc.sh"),
        "13": ("Install OBS", "obs.sh"),
        "14": ("Install NVIDIA drivers", "nvidia_drivers.sh"),
    }

    while True:
        print("\nPlease choose what you want to install:")

        for key, value in options.items():
            print(f"{key}. {value[0]}")

        choice = input("Enter your choice (or 'E' to exit): ").strip()

        if choice.lower() == "e":
            print("Exiting...")
            break

        if choice in options:
            script_name = options[choice][1]
            subprocess.run(["bash", script_name])
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
