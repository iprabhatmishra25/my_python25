import configparser
from datetime import datetime
from pathlib import Path


def main():
    config_file = Path("scan.ini")

    # 1. Create default scan.ini if it doesn't exist
    if not config_file.exists():
        config = configparser.ConfigParser()
        config["scan"] = {"directory": ".", "extension": ".py"}
        config["output"] = {"report_file": "scan_report.txt"}
        with open(config_file, "w") as f:
            config.write(f)
        print(f"Created default configuration file: {config_file.resolve()}")

    # 2. Read Configuration
    config = configparser.ConfigParser()
    config.read(config_file)

    scan_dir = Path(config.get("scan", "directory")).resolve()
    target_ext = config.get("scan", "extension").strip()
    if not target_ext.startswith("."):
        target_ext = f".{target_ext}"

    output_file = Path(config.get("output", "report_file"))

    if not scan_dir.is_dir():
        raise NotADirectoryError(f"Directory not found: {scan_dir}")

    # 3. Scan Directory
    report_lines = [
        f"Scan Report for: {scan_dir}",
        f"Target Extension: {target_ext}",
        f"Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 65,
        f"{'File Name':<35} | {'Size (KB)':<10} | {'Modified Date'}",
        "-" * 65,
    ]

    matched_files = 0
    for file_path in scan_dir.rglob(f"*{target_ext}"):
        if file_path.is_file():
            stats = file_path.stat()
            size_kb = stats.st_size / 1024
            mod_time = datetime.fromtimestamp(stats.st_mtime).strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            report_lines.append(
                f"{file_path.name:<35} | {size_kb:<10.2f} | {mod_time}"
            )
            matched_files += 1

    report_lines.append("-" * 65)
    report_lines.append(f"Total matching files found: {matched_files}")

    # 4. Write Output Report
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines) + "\n")

    print(f"Scan complete. Report saved to: {output_file.resolve()}")


if __name__ == "__main__":
    main()