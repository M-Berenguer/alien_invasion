# Alien Invasion

A game in python from the book "Python Crash Course" by Eric Matthes.

## Requirements

1. Install Pygame

    ```shell
    python -m pip install --user pygame
    ````

2. If you use Visual Studio Code and PyLint, you need adding settings to your project.

    You can add the settings directly to your workspace settings JSON file. Here is how you can do it:

    1. Open the Command Palette by pressing Ctrl+Shift+P.
    2. Type and select **Preferences: Open Workspace Settings (JSON)**.
    3. Add the following configuration to the JSON file:

        ```json
        {
            "pylint.args": [
                "--extension-pkg-whitelist=pygame"
            ]      
        }
        ```

    4. Save the file, and the settings will be applied immediately.

    With this configuration we avoid the appearance of problems that are not real, such as:

    ```log
     Module 'pygame' has no 'init' member #2502
     Module 'pygame' has no 'FULLSCREEN' member
     ...
    ```
