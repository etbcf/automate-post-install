#!/usr/bin/env python3

import subprocess
import time


def run_command(command, description):
    try:
        print(description)
        time.sleep(2)
        subprocess.run(command, shell=True, check=True)
        print("✅ Success!\n")
        time.sleep(2)
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


commands = [
    ("sudo dnf upgrade --refresh -y", "📦 Updating system..."),
    (
        "sudo dnf install -y "
        "https://download1.rpmfusion.org/free/fedora/"
        "rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm "
        "https://download1.rpmfusion.org/nonfree/fedora/"
        "rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm",
        "🔧 Enabling RPM Fusion repos...",
    ),
    (
        "sudo dnf config-manager setopt fedora-cisco-openh264.enabled=1",
        "🔧 Enabling openh264 repo...",
    ),
    (
        "sudo dnf install -y neovim vim-enhanced tmux git gnome-tweaks "
        "ripgrep fd-find fzf uv ruff the_silver_searcher trash-cli "
        "gnome-themes-extra @virtualization steam-devices fastfetch",
        "🧰 Installing essential tools...",
    ),
    (
        "flatpak install flathub -y "
        "org.signal.Signal org.videolan.VLC com.bitwarden.desktop "
        "com.valvesoftware.Steam com.mattjakeman.ExtensionManager",
        "📦 Installing Flatpak apps...",
    ),
    (
        'grep -qxF \'eval "$(fzf --bash)"\' "$HOME/.bashrc" || echo \'eval "$(fzf --bash)"\' >> "$HOME/.bashrc"',
        "🔧 Enabling fzf keybindings...",
    ),
    (
        "mkdir -p ~/.fonts && "
        "curl -L -o /tmp/FiraCode.zip https://github.com/ryanoasis/nerd-fonts/releases/latest/download/FiraCode.zip && "
        "unzip -o /tmp/FiraCode.zip -d ~/.fonts && "
        "fc-cache -fv && "
        "rm /tmp/FiraCode.zip",
        "🔣 Installing FiraCode Nerd Font...",
    ),
    ("sudo systemctl enable --now firewalld", "🔒 Enabling firewall..."),
    (
        "git clone --depth 1 https://github.com/etbcf/post-install.git /tmp/post-install && "
        'mv /tmp/post-install/.vimrc "$HOME/.vimrc" && '
        'mv /tmp/post-install/nvim "$HOME/.config/nvim" && '
        'mv /tmp/post-install/.tmux.conf "$HOME/.tmux.conf" && '
        'mv /tmp/post-install/.gitconfig "$HOME/.gitconfig" && '
        'mv /tmp/post-install/bin "$HOME/bin"',
        "📥 Cloning dotfiles from GitHub...",
    ),
    (
        "bash -c '"
        "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash && "
        'export NVM_DIR="$HOME/.nvm" && '
        '[ -s "$NVM_DIR/nvm.sh" ] && source "$NVM_DIR/nvm.sh" && '
        "nvm install --lts"
        "'",
        "⬇️ Installing Node.js via NVM...",
    ),
    (
        'bash -c "source $HOME/bin/functions"',
        "⚙️ Sourcing functions script...",
    ),
    (
        "curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim",
        "🔌 Installing vim-plug for Vim...",
    ),
    (
        "curl -sS https://starship.rs/install.sh | sh && "
        'grep -qxF \'eval "$(starship init bash)"\' "$HOME/.bashrc" || echo \'eval "$(starship init bash)"\' >> "$HOME/.bashrc"',
        "🚀 Installing Starship prompt...",
    ),
]

for cmd, desc in commands:
    run_command(cmd, desc)


def add_vscode_repo():
    repo_content = """[code]
name=Visual Studio Code
baseurl=https://packages.microsoft.com/yumrepos/vscode
enabled=1
autorefresh=1
type=rpm-md
gpgcheck=1
gpgkey=https://packages.microsoft.com/keys/microsoft.asc
"""

    # Write repo file
    with open("/tmp/vscode.repo", "w") as f:
        f.write(repo_content)

    # Import key and move repo file
    subprocess.run(
        "sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc",
        shell=True,
        check=True,
    )
    subprocess.run(
        "sudo mv /tmp/vscode.repo /etc/yum.repos.d/vscode.repo", shell=True, check=True
    )

    # Update and install
    subprocess.run("sudo dnf check-update", shell=True, check=True)
    subprocess.run("sudo dnf install -y code", shell=True, check=True)


print("💻 Installing Visual Studio Code...")
try:
    add_vscode_repo()
    print("✅ Visual Studio Code installed!")
except Exception as e:
    print(f"❌ Failed to install VS Code: {e}")

print("✅ All done. You may want to reboot now.")
