"""
Somatosensory Hoffmann Reflex (H-Reflex) & Spinal Motoneuron Excitability Engine.
Provides deterministic, zero-dependency modeling of Hmax / Mmax amplitude ratio,
H-reflex onset latency (ms), presynaptic inhibition, and spinal alpha motoneuron pool neuromuscular excitability.
"""

from typing import Dict, Any, List, Optional


class SomatosensoryHReflexClient:
    """
    Deterministic client for calculating Hoffmann Reflex (H-Reflex) excitability and conduction kinetics.
    Assesses group Ia afferent sensory fibers, monosynaptic spinal cord transmission,
    alpha motoneuron pool recruitment, and central neuromuscular fatigue.
    """

    def __init__(self):
        pass

    def evaluate_h_reflex(
        self,
        h_max_amplitude_mv: float,
        m_max_amplitude_mv: float,
        h_latency_ms: float = 30.0,
        stimulation_nerve: str = "TIBIAL_NERVE_SOLEUS"
    ) -> Dict[str, Any]:
        """
        Calculates Hmax/Mmax ratio and evaluates spinal motoneuron pool excitability.
        Normative values (Tibial nerve / Soleus muscle at rest):
        - Hmax / Mmax ratio: 0.40 - 0.70 (40.0% - 70.0%)
        - H-reflex onset latency: 28.0 - 34.0 ms (S1 nerve root)
        - Latency > 36.0 ms suggests peripheral conduction slowing or radiculopathy
        - Ratio > 0.80 suggests hyper-reflexia / spasticity
        - Ratio < 0.25 suggests central fatigue, hyporeflexia, or sensory axonal loss
        """
        if h_max_amplitude_mv < 0 or m_max_amplitude_mv <= 0:
            return {"error": "Hmax must be non-negative and Mmax must be strictly positive"}
        if h_max_amplitude_mv > m_max_amplitude_mv * 1.2:
            return {"error": "Hmax amplitude cannot unrealistically exceed supramaximal M-wave"}
        if h_latency_ms <= 0:
            return {"error": "H-reflex latency must be positive"}

        # Hmax / Mmax amplitude ratio
        h_m_ratio = round(h_max_amplitude_mv / m_max_amplitude_mv, 3)
        h_m_ratio_pct = round(h_m_ratio * 100.0, 1)

        # Spinal Motoneuron Excitability Score (0 - 100)
        score = 80.0
        if 0.40 <= h_m_ratio <= 0.70:
            score += 15.0
        elif 0.30 <= h_m_ratio < 0.40 or 0.70 < h_m_ratio <= 0.78:
            score += 5.0
        elif h_m_ratio > 0.85:
            score -= 25.0  # Hyper-excitability / spastic tone
        elif h_m_ratio < 0.20:
            score -= 28.0  # Profound depression / central fatigue

        if 28.0 <= h_latency_ms <= 33.5:
            score += 5.0
        elif h_latency_ms > 36.5:
            score -= 20.0
        elif h_latency_ms > 34.5:
            score -= 10.0

        spinal_score = round(min(100.0, max(5.0, score)), 1)

        if spinal_score >= 85.0 and 0.40 <= h_m_ratio <= 0.70 and h_latency_ms <= 34.0:
            tier = "OPTIMAL_SPINAL_MOTONEURON_EXCITABILITY"
            interp = f"Balanced monosynaptic reflex arc (Hmax/Mmax {h_m_ratio_pct}%, Latency {h_latency_ms} ms); optimal presynaptic inhibition and alpha motoneuron recruitment."
            guidance = "Normal spinal reflex transmission. Neuromuscular recovery and central drive are balanced."
        elif h_m_ratio < 0.25:
            tier = "DEPRESSED_SPINAL_EXCITABILITY_OR_FATIGUE"
            interp = f"Significant reduction in reflex ratio (Hmax/Mmax {h_m_ratio_pct}% < 25%); indicates central neural drive depletion, post-activation depression, or Ia afferent fatigue."
            guidance = "Neuromuscular central fatigue detected. Avoid high-load explosive contractions; schedule passive stretching and systemic recovery."
        elif h_m_ratio > 0.80:
            tier = "SPINAL_HYPER_EXCITABILITY_SPASTICITY"
            interp = f"Elevated reflex excitability (Hmax/Mmax {h_m_ratio_pct}% > 80%); reflects attenuated descending presynaptic inhibition or hyper-reflexic state."
            guidance = "Elevated spinal motoneuron excitability. Practice down-regulating breathwork and gentle foam rolling to modulate muscle spindle tone."
        else:
            tier = "DELAYED_H_REFLEX_CONDUCTION"
            interp = f"Prolonged reflex latency ({h_latency_ms} ms > 34.0 ms); suggests S1 radicular compromise or peripheral nerve conduction delay."
            guidance = "Slowed reflex transmission. Screen for lumbar disc protrusion or sciatic nerve compression."

        return {
            "stimulation_nerve": stimulation_nerve,
            "h_max_amplitude_mv": h_max_amplitude_mv,
            "m_max_amplitude_mv": m_max_amplitude_mv,
            "h_m_ratio": h_m_ratio,
            "h_m_ratio_pct": h_m_ratio_pct,
            "h_latency_ms": h_latency_ms,
            "spinal_excitability_score": spinal_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
