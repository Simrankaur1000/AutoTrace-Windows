# AutoTrace-Windows

A Windows digital-forensics utility for collecting selected user-activity artefacts and exporting them as JSON for review.

## Capabilities

- Collects Chrome and Microsoft Edge browsing history for the configured recent period (currently 30 days).
- Extracts failed logon events from the Windows Security event log.
- Exports collected artefacts to JSON for further analysis.
- Designed for Windows environments; elevated privileges may be required to access Security logs.

## Requirements

- Windows
- Python 3.10+
- Administrator privileges for Security event-log access
- Chrome and/or Edge data available locally

## Setup

```powershell
git clone https://github.com/Simrankaur1000/AutoTrace-Windows.git
cd AutoTrace-Windows
pip install -r requirements.txt
python main.py
```

## Forensic considerations

- Run only on systems you own or are explicitly authorized to examine.
- Preserve original artefacts and document collection time, host, and operator.
- Treat exported JSON as sensitive evidence; restrict access and maintain integrity hashes when using it in an investigation.
- Browser databases may be locked while the browser is running; close browsers before collection.

## Scope and limitations

This is a focused collection utility, not a full forensic acquisition suite. It does not replace validated forensic imaging, chain-of-custody procedures, or specialist forensic analysis.

## Author

Simran Kaur · [Portfolio](https://portfolio-k3wf.vercel.app)
