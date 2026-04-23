import json
from collections import defaultdict

# =========================
# Innerlytics Engine
# =========================

class InnerlyticsAgent:
    def __init__(self, tree_file):
        with open(tree_file, "r") as f:
            data = json.load(f)

        self.nodes = {node["id"]: node for node in data["nodes"]}
        self.state = {
            "answers": {},
            "signals": defaultdict(lambda: defaultdict(int))
        }

    # -------------------------
    # Utility: Print nicely
    # -------------------------
    def display(self, text):
        print("\n" + text)

    # -------------------------
    # Input handling
    # -------------------------
    def ask_question(self, node):
        self.display(node["text"])

        options = node.get("options", [])
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")

        while True:
            try:
                choice = int(input("Select option: "))
                if 1 <= choice <= len(options):
                    answer = options[choice - 1]
                    self.state["answers"][node["id"]] = answer
                    return answer
            except:
                pass
            print("Invalid input. Try again.")

    # -------------------------
    # Signal processing
    # -------------------------
    def apply_signal(self, signal):
        if not signal:
            return

        axis, value = signal.split(":")
        self.state["signals"][axis][value] += 1

    # -------------------------
    # Determine dominant
    # -------------------------
    def get_dominant(self, axis):
        axis_data = self.state["signals"].get(axis, {})
        if not axis_data:
            return "neutral"
        return max(axis_data, key=axis_data.get)

    # -------------------------
    # Decision routing
    # -------------------------
    def handle_decision(self, node, prev_answer):
        rules = node.get("rules", [])

        for rule in rules:
            if prev_answer in rule["if"]:
                return rule["goto"]

        raise Exception(f"No rule matched for decision node {node['id']}")

    # -------------------------
    # Get next node (default)
    # -------------------------
    def get_next_node(self, current_id):
        for node in self.nodes.values():
            if node.get("parentId") == current_id:
                return node["id"]
        return None

    # -------------------------
    # String Interpolation
    # -------------------------
    def interpolate_text(self, text):
        import re
        # replace answer placeholders
        matches = re.findall(r"\{([\w_]+)\.answer\}", text)
        for node_id in matches:
            val = self.state["answers"].get(node_id, "")
            text = text.replace(f"{{{node_id}.answer}}", val)
            
        # replace dominant placeholders
        text = text.replace("{axis1.dominant}", self.get_dominant("axis1"))
        text = text.replace("{axis2.dominant}", self.get_dominant("axis2"))
        text = text.replace("{axis3.dominant}", self.get_dominant("axis3"))
        return text

    # -------------------------
    # Run Engine
    # -------------------------
    def run(self):
        current_id = "START"
        prev_answer = None

        while current_id:
            node = self.nodes[current_id]
            node_type = node["type"]

            # START / BRIDGE / REFLECTION
            if node_type in ["start", "bridge", "reflection"]:
                self.display(self.interpolate_text(node["text"]))
                self.apply_signal(node.get("signal"))

                # bridge override
                if "target" in node:
                    current_id = node["target"]
                else:
                    current_id = self.get_next_node(current_id)

            # QUESTION
            elif node_type == "question":
                node["text"] = self.interpolate_text(node["text"])
                answer = self.ask_question(node)
                prev_answer = answer
                self.apply_signal(node.get("signal"))
                current_id = self.get_next_node(current_id)

            # DECISION
            elif node_type == "decision":
                current_id = self.handle_decision(node, prev_answer)

            # SUMMARY
            elif node_type == "summary":
                summary = self.interpolate_text(node["text"])
                self.display(summary)
                
                # allow target override for summary
                if "target" in node:
                    current_id = node["target"]
                else:
                    current_id = self.get_next_node(current_id)

            # END
            elif node_type == "end":
                self.display(self.interpolate_text(node["text"]))
                break

            else:
                raise Exception(f"Unknown node type: {node_type}")


# =========================
# Entry Point
# =========================

if __name__ == "__main__":
    print("\n✨ Innerlytics Reflection Agent ✨")
    print("----------------------------------")

    agent = InnerlyticsAgent("../tree/reflection-tree.json")
    agent.run()