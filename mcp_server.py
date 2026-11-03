"""
MCP Server for Somatosensory Hoffmann Reflex (H-Reflex) Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating Hmax/Mmax ratios, reflex latencies, and spinal excitability scores.
"""

import sys
import json
from typing import Dict, Any
from client import SomatosensoryHReflexClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_h_reflex",
                "description": "Calculates Hoffmann Reflex (H-Reflex) Hmax/Mmax amplitude ratio (%), onset latency (ms), and spinal alpha motoneuron excitability score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "h_max_amplitude_mv": {
                            "type": "number",
                            "description": "Maximal H-reflex amplitude in millivolts (e.g. 4.2 mV)."
                        },
                        "m_max_amplitude_mv": {
                            "type": "number",
                            "description": "Supramaximal M-wave amplitude in millivolts (e.g. 8.0 mV)."
                        },
                        "h_latency_ms": {
                            "type": "number",
                            "description": "H-reflex onset latency in milliseconds (e.g. 30.2 ms, normative 28-34 ms, default: 30.0 ms).",
                            "default": 30.0
                        },
                        "stimulation_nerve": {
                            "type": "string",
                            "description": "Target nerve and muscle site (default: TIBIAL_NERVE_SOLEUS).",
                            "default": "TIBIAL_NERVE_SOLEUS"
                        }
                    },
                    "required": ["h_max_amplitude_mv", "m_max_amplitude_mv"]
                }
            }
        ]
    }


def handle_request(client: SomatosensoryHReflexClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_h_reflex":
            res = client.evaluate_h_reflex(
                h_max_amplitude_mv=float(args.get("h_max_amplitude_mv", 4.0)),
                m_max_amplitude_mv=float(args.get("m_max_amplitude_mv", 8.0)),
                h_latency_ms=float(args.get("h_latency_ms", 30.0)),
                stimulation_nerve=str(args.get("stimulation_nerve", "TIBIAL_NERVE_SOLEUS"))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = SomatosensoryHReflexClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
