# upgrade_manager.py - Manages upgrade choices and effectiveness tracking

import json
import os

class UpgradeManager:
    def __init__(self, db_path='upgrade_db.json'):
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            self._initialize_db()
        else:
            with open(self.db_path, 'r') as f:
                self.upgrade_data = json.load(f)

    def _initialize_db(self):
        # Initialize an empty database
        self.upgrade_data = {}
        self._save_db()

    def _save_db(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.upgrade_data, f, indent=4)

    def update_upgrade_choice(self, upgrade_name, effectiveness):
        # Create entry if not exists
        if upgrade_name not in self.upgrade_data:
            self.upgrade_data[upgrade_name] = {
                'times_chosen': 0,
                'cumulative_effectiveness': 0.0
            }
        
        # Update the upgrade data
        self.upgrade_data[upgrade_name]['times_chosen'] += 1
        self.upgrade_data[upgrade_name]['cumulative_effectiveness'] += effectiveness

        # Print choice result
        print(f"🔼 Chose upgrade: {upgrade_name}, Effectiveness: {effectiveness}")

        # Save changes
        self._save_db()

    def evaluate_best_upgrade(self, available_upgrades):
        """Evaluate available upgrades and return both name and index"""
        # Only consider the first 3 options (main upgrade choices)
        main_upgrades = available_upgrades[:3] if len(available_upgrades) >= 3 else available_upgrades
        
        best_upgrade = None
        best_score = -float('inf')
        best_index = 0
        
        print(f"🔍 Evaluating {len(main_upgrades)} main upgrade options:")

        for i, upgrade_name in enumerate(main_upgrades):
            if upgrade_name in self.upgrade_data:
                # Calculate average effectiveness
                record = self.upgrade_data[upgrade_name]
                average_effectiveness = record['cumulative_effectiveness'] / record['times_chosen']
                times_chosen = record['times_chosen']
            else:
                # New upgrade gets a small bonus to encourage exploration
                average_effectiveness = 0.5  # Slight bonus for new options
                times_chosen = 0

            print(f"  {i+1}. {upgrade_name}: Avg={average_effectiveness:.2f}, Times={times_chosen}")

            # Choose the best upgrade (with exploration bonus for new options)
            if average_effectiveness > best_score:
                best_score = average_effectiveness
                best_upgrade = upgrade_name
                best_index = i

        # Ensure index is within valid range (0-2)
        if best_index > 2:
            print(f"⚠️ Index {best_index} out of range, using option 1")
            best_index = 0
            best_upgrade = main_upgrades[0] if main_upgrades else "Option 1"

        print(f"🎯 Best choice: {best_upgrade} (option {best_index + 1}) with score {best_score:.2f}")
        return best_upgrade, best_index
    
    def get_upgrade_stats(self):
        """Get statistics about all upgrades in the database"""
        if not self.upgrade_data:
            return "No upgrade data available yet."
        
        stats = []
        stats.append("📊 UPGRADE STATISTICS:")
        stats.append("=" * 40)
        
        # Sort by effectiveness
        sorted_upgrades = sorted(
            self.upgrade_data.items(),
            key=lambda x: x[1]['cumulative_effectiveness'] / x[1]['times_chosen'],
            reverse=True
        )
        
        for upgrade_name, data in sorted_upgrades:
            avg_eff = data['cumulative_effectiveness'] / data['times_chosen']
            stats.append(f"{upgrade_name:20} | Avg: {avg_eff:5.2f} | Count: {data['times_chosen']:3d}")
        
        return "\n".join(stats)

