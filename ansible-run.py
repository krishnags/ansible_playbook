---
- name: Retrieve Python Script from GitHub and Run on Target Servers
  hosts: Demo Inventory  # Replace with your target group or hosts
  become: yes  # Run tasks as the root user

  tasks:
    # Clone the GitHub repository to a temporary directory
    - name: Clone GitHub Repository
      community.general.github_repository:
        repo: 'krishnags/python-test'  # Replace with your GitHub username and repository name
        dest: '/tmp'  # Specify the destination directory on the target servers
        version: main  # Specify the branch or tag if needed

    # Copy the Python script to the target location
    - name: Copy Python Script to Target Location
      copy:
        src: '/tmp/python-test.py'  # Replace with the path to your Python script in the repository
        dest: '/tmp/python-test.py'  # Specify the destination path on the target servers
        mode: '0755'  # Set appropriate permissions

    # Execute the Python script on the target servers
    - name: Execute Python Script
      command: python /tmp/python-test.py
