# Somatosensory Hoffmann Reflex (H-Reflex) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Hoffmann Reflex (H-Reflex) $H_{max} / M_{max}$ recruitment ratio, reflex onset latency, and spinal alpha motoneuron pool neuromuscular excitability.

```mermaid
flowchart TD
    IaStim["Submaximal Ia Afferent Electrical Stimulation (Tibial Nerve)"] --> MonoSynapse["Spinal Cord Monosynaptic Synapse (Ventral Horn)"]
    MonoSynapse --> AlphaMotoneuron["Alpha Motoneuron Pool Recruitment"]
    AlphaMotoneuron --> H_Wave["Soleus EMG H-Reflex Wave (Latency ~30 ms)"]
    MaxDirectStim["Supramaximal Direct Motor Axon Stim"] --> M_Wave["Maximal Direct Muscle M-Wave"]
    H_Wave & M_Wave --> RatioCalc["Hmax / Mmax Ratio Engine & Central Fatigue Score"]
    RatioCalc --> Agent["OpenClaw / Hermes Personal Agent Recovery Guarding"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Electroneuromyography (ENMG) Standards**: Formulates Hmax/Mmax recruitment curves, monosynaptic transmission latency, and presynaptic inhibition.
- **Central Neuromuscular Fatigue**: Highly sensitive detection of spinal motoneuron exhaustion vs peripheral muscle fatigue.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import SomatosensoryHReflexClient

client = SomatosensoryHReflexClient()
result = client.evaluate_h_reflex(
    h_max_amplitude_mv=4.2,
    m_max_amplitude_mv=7.8,
    h_latency_ms=30.4
)
print("Hmax / Mmax Ratio:", result["h_m_ratio_pct"], "%")
print("Spinal Excitability Score:", result["spinal_excitability_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
