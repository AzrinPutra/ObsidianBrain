# EDR vs Traditional Antivirus Analysis

## Comparison Dimensions
1. **Detection Methodology**
   - AV: Signature-based detection
   - EDR: Behavioral analysis + threat intelligence

2. **Response Capabilities**
   - AV: Quarantine/delete files
   - EDR: Endpoint isolation, process termination, forensic rollback

3. **Threat Coverage**
   - AV: Known malware patterns
   - EDR: Zero-day, fileless, and living-off-the-land attacks

4. **Visibility**
   - AV: Basic file scanning
   - EDR: Full endpoint activity monitoring

5. **Resource Footprint**
   - AV: Low CPU/RAM usage
   - EDR: Continuous monitoring requires more resources

## Knowledge Gaps Identified
- No existing vault documentation on MITRE ATT&CK framework integration
- Limited coverage of EDR false positive management strategies
- No comparative analysis of leading EDR solutions (CrowdStrike vs Cylance vs SentinelOne)
- EDR threat hunting workflows
- AV signature update mechanisms
- Cloud integration capabilities