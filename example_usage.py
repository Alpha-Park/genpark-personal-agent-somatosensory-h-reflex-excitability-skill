"""
Example Usage: Somatosensory Hoffmann Reflex (H-Reflex).
Demonstrates zero-dependency calculation of Hmax/Mmax ratio, latency, and spinal excitability scoring.
"""

from client import SomatosensoryHReflexClient


def main():
    client = SomatosensoryHReflexClient()
    print("=== Somatosensory Hoffmann Reflex (H-Reflex) Demo ===")

    # Test Case 1: Healthy resting soleus H-reflex
    res1 = client.evaluate_h_reflex(
        h_max_amplitude_mv=4.2,
        m_max_amplitude_mv=7.8,
        h_latency_ms=30.4,
        stimulation_nerve="TIBIAL_NERVE_SOLEUS"
    )
    print("\nTest Case 1: Normal Spinal Excitability (Tibial / Soleus)")
    print(f"  Hmax Amplitude: {res1['h_max_amplitude_mv']} mV | Mmax Amplitude: {res1['m_max_amplitude_mv']} mV")
    print(f"  Hmax / Mmax Ratio: {res1['h_m_ratio']} ({res1['h_m_ratio_pct']}%)")
    print(f"  H-Reflex Latency: {res1['h_latency_ms']} ms")
    print(f"  Spinal Excitability Score: {res1['spinal_excitability_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Depressed reflex / central neuromuscular fatigue
    res2 = client.evaluate_h_reflex(
        h_max_amplitude_mv=1.2,
        m_max_amplitude_mv=7.5,
        h_latency_ms=31.2,
        stimulation_nerve="TIBIAL_NERVE_SOLEUS"
    )
    print("\nTest Case 2: Post-Exertional Central Fatigue Pattern")
    print(f"  Hmax / Mmax Ratio: {res2['h_m_ratio']} ({res2['h_m_ratio_pct']}%)")
    print(f"  Spinal Excitability Score: {res2['spinal_excitability_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
