@echo off
setlocal EnableDelayedExpansion

REM MobileShop-Dashboard Setup and Management Script for Windows
REM Version: 1.0.0
REM Description: Automated setup, development, and deployment script for Windows

set PROJECT_NAME=MobileShop-Dashboard
set PYTHON_VERSION=3.8
set VENV_NAME=mobileshop_env
set MAIN_FILE=main.py

REM ANSI color codes for Windows 10+
set "RED=[91m"
set "GREEN=[92m"
set "YELLOW=[93m"
set "BLUE=[94m"
set "PURPLE=[95m"
set "CYAN=[96m"
set "NC=[0m"

:banner
echo.
echo %CYAN%  ╔════════════════════════════════════════════════════════════╗%NC%
echo %CYAN%  ║                    📱 Mobile Shop Dashboard                 ║%NC%
echo %CYAN%  ║                   Windows Setup Script                     ║%NC%
echo %CYAN%  ║                        Version 1.0.0                      ║%NC%
echo %CYAN%  ╚════════════════════════════════════════════════════════════╝%NC%
echo.
goto :eof

:log_info
echo %BLUE%[INFO]%NC% %1
goto :eof

:log_success
echo %GREEN%[SUCCESS]%NC% %1
goto :eof

:log_warning
echo %YELLOW%[WARNING]%NC% %1
goto :eof

:log_error
echo %RED%[ERROR]%NC% %1
goto :eof

:log_step
echo %PURPLE%[STEP]%NC% %1
goto :eof

:check_python
call :log_step "Checking Python installation..."

python --version >nul 2>&1
if !errorlevel! neq 0 (
    py --version >nul 2>&1
    if !errorlevel! neq 0 (
        call :log_error "Python is not installed. Please install Python %PYTHON_VERSION%+ from python.org"
        pause
        exit /b 1
    ) else (
        set PYTHON_CMD=py
    )
) else (
    set PYTHON_CMD=python
)

for /f "tokens=2 delims= " %%i in ('%PYTHON_CMD% --version 2^>^&1') do set PYTHON_VER=%%i
call :log_info "Found Python !PYTHON_VER!"

REM Check if Python version is 3.8+
%PYTHON_CMD% -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)" >nul 2>&1
if !errorlevel! neq 0 (
    call :log_error "Python %PYTHON_VERSION%+ is required. Current version: !PYTHON_VER!"
    pause
    exit /b 1
)

call :log_success "Python version check passed"
goto :eof

:setup_venv
call :log_step "Setting up virtual environment..."

if not exist "%VENV_NAME%" (
    call :log_info "Creating virtual environment: %VENV_NAME%"
    %PYTHON_CMD% -m venv %VENV_NAME%
    if !errorlevel! neq 0 (
        call :log_error "Failed to create virtual environment"
        exit /b 1
    )
    call :log_success "Virtual environment created"
) else (
    call :log_warning "Virtual environment already exists"
)

REM Activate virtual environment
call %VENV_NAME%\Scripts\activate.bat
if !errorlevel! neq 0 (
    call :log_error "Failed to activate virtual environment"
    exit /b 1
)

call :log_success "Virtual environment activated"
goto :eof

:install_dependencies
call :log_step "Installing dependencies..."

REM Upgrade pip
call :log_info "Upgrading pip..."
python -m pip install --upgrade pip
if !errorlevel! neq 0 (
    call :log_warning "Failed to upgrade pip, continuing..."
)

REM Create requirements.txt if it doesn't exist
if not exist "requirements.txt" (
    call :log_info "Creating requirements.txt..."
    (
        echo PyQt6^>=6.0.0
        echo matplotlib^>=3.5.0
    ) > requirements.txt
    call :log_success "requirements.txt created"
)

REM Install requirements
call :log_info "Installing packages from requirements.txt..."
pip install -r requirements.txt
if !errorlevel! neq 0 (
    call :log_error "Failed to install dependencies"
    exit /b 1
)

call :log_success "Dependencies installed successfully"
goto :eof

:create_structure
call :log_step "Creating project structure..."

REM Create directories
if not exist "screenshots" mkdir screenshots
if not exist "docs" mkdir docs
if not exist "tests" mkdir tests
if not exist "assets" mkdir assets

REM Create main.py if it doesn't exist
if not exist "%MAIN_FILE%" (
    call :log_warning "main.py not found. You need to add your application code."
    type nul > %MAIN_FILE%
)

REM Create .gitignore
if not exist ".gitignore" (
    call :log_info "Creating .gitignore..."
    (
        echo # Virtual Environment
        echo %VENV_NAME%/
        echo venv/
        echo env/
        echo.
        echo # Python
        echo __pycache__/
        echo *.py[cod]
        echo *$py.class
        echo *.so
        echo .Python
        echo build/
        echo develop-eggs/
        echo dist/
        echo downloads/
        echo eggs/
        echo .eggs/
        echo lib/
        echo lib64/
        echo parts/
        echo sdist/
        echo var/
        echo wheels/
        echo *.egg-info/
        echo .installed.cfg
        echo *.egg
        echo MANIFEST
        echo.
        echo # PyQt
        echo *.ui~
        echo *.qrc~
        echo.
        echo # IDE
        echo .vscode/
        echo .idea/
        echo *.swp
        echo *.swo
        echo *~
        echo.
        echo # OS
        echo .DS_Store
        echo Thumbs.db
        echo.
        echo # Logs
        echo *.log
        echo logs/
    ) > .gitignore
    call :log_success ".gitignore created"
)

call :log_success "Project structure created"
goto :eof

:run_app
call :log_step "Starting MobileShop-Dashboard..."

if not exist "%MAIN_FILE%" (
    call :log_error "main.py not found. Please ensure the application file exists."
    pause
    exit /b 1
)

REM Activate virtual environment if not already active
if "%VIRTUAL_ENV%"=="" (
    call %VENV_NAME%\Scripts\activate.bat
)

call :log_info "Launching application..."
python %MAIN_FILE%
goto :eof

:run_tests
call :log_step "Running tests..."

if not exist "tests" (
    call :log_warning "No tests directory found. Creating basic test structure..."
    mkdir tests
    type nul > tests\__init__.py
    (
        echo import unittest
        echo import sys
        echo import os
        echo.
        echo # Add parent directory to path
        echo sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        echo.
        echo class TestBasic(unittest.TestCase):
        echo     def test_import(self):
        echo         """Test if main module can be imported"""
        echo         try:
        echo             # Import your main module here
        echo             # import main
        echo             pass
        echo         except ImportError as e:
        echo             self.fail(f"Failed to import main module: {e}"^)
        echo.
        echo if __name__ == '__main__':
        echo     unittest.main(^)
    ) > tests\test_basic.py
    call :log_success "Basic test structure created"
)

call :log_info "Executing tests..."
python -m unittest discover tests\ -v
goto :eof

:clean_project
call :log_step "Cleaning project..."

REM Remove Python cache
for /d /r %%i in (__pycache__) do (
    if exist "%%i" (
        rmdir /s /q "%%i" 2>nul
    )
)

del /s /q *.pyc 2>nul
del /s /q *.pyo 2>nul

REM Remove build artifacts
if exist "build" rmdir /s /q build 2>nul
if exist "dist" rmdir /s /q dist 2>nul
for /d %%i in (*.egg-info) do (
    if exist "%%i" rmdir /s /q "%%i" 2>nul
)

call :log_success "Project cleaned"
goto :eof

:show_system_info
call :log_step "System Information"
echo ========================
echo OS: Windows
%PYTHON_CMD% --version 2>&1
pip --version 2>&1

if exist "%VENV_NAME%" (
    echo Virtual Environment: ✅ %VENV_NAME%
) else (
    echo Virtual Environment: ❌ Not found
)

if exist "requirements.txt" (
    echo Requirements: ✅ Found
) else (
    echo Requirements: ❌ Not found
)

if exist "%MAIN_FILE%" (
    echo Main Application: ✅ %MAIN_FILE%
) else (
    echo Main Application: ❌ Not found
)
echo ========================
goto :eof

:show_help
echo.
echo %CYAN%MobileShop-Dashboard Management Script for Windows%NC%
echo.
echo Usage: README.bat [COMMAND]
echo.
echo %YELLOW%Available Commands:%NC%
echo   setup         - Complete project setup (venv, dependencies, structure)
echo   install       - Install/update dependencies
echo   run           - Run the application
echo   test          - Run tests
echo   clean         - Clean project (remove cache, build files)
echo   info          - Show system information
echo   help          - Show this help message
echo.
echo %YELLOW%Examples:%NC%
echo   README.bat setup      # Initial project setup
echo   README.bat run        # Run the application
echo   README.bat clean      # Clean project files
echo.
echo %YELLOW%Development Workflow:%NC%
echo   1. Run 'README.bat setup' for initial setup
echo   2. Run 'README.bat run' to start the application
echo   3. Run 'README.bat test' to run tests
echo   4. Run 'README.bat clean' before committing
echo.
goto :eof

:main
call :banner

if "%1"=="" goto help
if "%1"=="setup" goto setup
if "%1"=="install" goto install
if "%1"=="run" goto run
if "%1"=="test" goto test
if "%1"=="clean" goto clean
if "%1"=="info" goto info
if "%1"=="help" goto help
if "%1"=="--help" goto help
if "%1"=="-h" goto help

call :log_error "Unknown command: %1"
echo.
goto help

:setup
call :check_python
call :setup_venv
call :install_dependencies
call :create_structure
call :log_success "Setup completed successfully! Run 'README.bat run' to start the application."
pause
goto :eof

:install
call :check_python
call :setup_venv
call :install_dependencies
pause
goto :eof

:run
call :run_app
pause
goto :eof

:test
call :run_tests
pause
goto :eof

:clean
call :clean_project
pause
goto :eof

:info
call :show_system_info
pause
goto :eof

:help
call :show_help
pause
goto :eof

call :main %1