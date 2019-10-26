# Protocol buffers

Protocol buffers allow code to be generated for many languages.

## Instructions

### Python

To update the python generated code used by the server according to the _.proto_ files, follow these steps:

1. Install the requirements.

    ```bash
    pip install -r requirements/production.txt
    ```
    
1. Run the `generate_grpc_python.sh` executable found in this directory.

    ```bash
    cd protobuf
    sh generate_grpc_python.sh
    ```
