class AccessibilityController:
    def __init__(self):
        self.switch_map = {
            "SWITCH_1": "NEXT_ITEM",
            "SWITCH_2": "SELECT",
            "SWITCH_3": "PREVIOUS_ITEM"
        }

    def map_switch_to_action(self, switch_id: str):
        """Maps a physical switch input to a logical UI action."""
        return self.switch_map.get(switch_id, "UNKNOWN")

    def generate_navigation_grid(self, screen_width, screen_height, grid_size=3):
        """Generates a grid for switch-based cursor navigation."""
        cells = []
        cell_w = screen_width // grid_size
        cell_h = screen_height // grid_size
        
        for r in range(grid_size):
            for c in range(grid_size):
                cells.append({
                    "id": f"grid_{r}_{c}",
                    "x": c * cell_w,
                    "y": r * cell_h,
                    "w": cell_w,
                    "h": cell_h
                })
        return cells
