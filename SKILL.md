---
name: genpark-personal-agent-somatosensory-h-reflex-excitability-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Hoffmann Reflex (H-Reflex) Hmax/Mmax amplitude ratio, reflex latency, and spinal alpha motoneuron pool neuromuscular excitability.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Somatosensory Hoffmann Reflex (H-Reflex) Skill

A sovereign personal agent capability for evaluating monosynaptic spinal reflex transmission, group Ia afferent sensory fiber conduction, alpha motoneuron pool excitability, and the $H_{max} / M_{max}$ recruitment ratio.

## Core Capabilities
- **Hmax / Mmax Amplitude Ratio**: Calculates relative spinal reflex excitability ($H_{max} / M_{max} \times 100\%$, normative: $40 - 70\%$).
- **Monosynaptic Reflex Latency**: Evaluates S1 nerve root conduction velocity and onset latency ($28.0 - 34.0\text{ ms}$).
- **Central Neuromuscular Fatigue Detection**: Identifies acute suppression of spinal alpha motoneuron excitability following intense exertion or prolonged postural load.
- **Spinal Down-Regulation Coaching**: Recommends parasympathetic breathing, gentle myofascial release, and neuromuscular rest when hyper-reflexic spasticity is detected.

## Fast Invocation
```python
from client import SomatosensoryHReflexClient

client = SomatosensoryHReflexClient()
res = client.evaluate_h_reflex(
    h_max_amplitude_mv=4.2,
    m_max_amplitude_mv=7.8,
    h_latency_ms=30.4
)
print("Hmax/Mmax Ratio:", res["h_m_ratio_pct"], "%")
print("Spinal Score:", res["spinal_excitability_score"], "/ 100")
```
