import os
import subprocess
from tests.utils import jira_aio_upload
from infra.secret_handler import SecretHandler


# Function to list all test files in the 'tests' directory
def list_test_files(test_dir='tests'):
    return [f for f in os.listdir(test_dir) if f.startswith('test_') and f.endswith('.py')]


# Function to display available test files and let the user select which ones to run
def select_test_files(test_files):
    print("Available test files:")
    for i, test_file in enumerate(test_files, start=1):
        print(f"{i}. {test_file}")

    selected_indices = input("Enter the numbers of the test files to run, separated by commas: ")
    selected_indices = [int(index.strip()) for index in selected_indices.split(',')]

    selected_files = [test_files[i - 1] for i in selected_indices if 0 < i <= len(test_files)]
    return selected_files


# Function to run pytest on selected test files and generate XML report
def run_pytest(selected_files, test_dir='tests'):
    files_to_run = [os.path.join(test_dir, f) for f in selected_files]
    command = ['pytest', '--log-cli-level=INFO', '--junitxml=report.xml'] + files_to_run
    subprocess.run(command)


if __name__ == '__main__':
    secret = SecretHandler.load_from_file()
    tests = list_test_files()  # List all available test files
    selected_tests = select_test_files(tests)  # Allow user to select test files
    run_pytest(selected_tests)  # Run pytest on the selected test files
    jira_aio_upload(secret['jira_aio_token'], secret['jira_aio_cycle'])  # Upload the test results
