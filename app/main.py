import subprocess

import modal

stub = modal.Stub("modal-arbitrary-code-example")


@stub.function(
    mounts=[
        modal.Mount.from_local_dir(
            local_path="./rust",
            remote_path="/root/rust",
        )
    ],
)
def run_rs() -> None:
    subprocess.run(["chmod", "+x", "/root/rust/bin/x86/app"])
    subprocess.run(["/root/rust/bin/x86/app"])


@stub.function(
    image=modal.Image.debian_slim().apt_install("ruby-full"),
    mounts=[
        modal.Mount.from_local_dir(
            local_path="./ruby",
            remote_path="/root/ruby",
        )
    ],
)
def run_rb() -> None:
    subprocess.run(["chmod", "+x", "/root/ruby/app.rb"])
    subprocess.run(["ruby", "/root/ruby/app.rb"])


@stub.local_entrypoint
def main() -> None:
    """Main entrypoint."""
    run_rs.call()
    run_rb.call()
