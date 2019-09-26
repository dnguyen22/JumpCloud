from action import Action
from rwlock import RWLock 
import json


class Solution(object):
	
	def __init__(self):
		self.database = {}
		self.lock = RWLock()

	def add_action(self, action):
		"""
		Adds a new action to the database.

		:param action: string formatted json object. Ex. '{"action":"jump", "time":100}'
		:return: None
		"""

		action_json = json.loads(action)
		action_name = action_json.get('action', '')
		action_duration = action_json.get('time', 0)

		with self.lock.w_locked():
			if action_name in self.database:
				self.database[action_name].add(action_duration)
			else:
				new_action = Action(action_name, action_duration)
				self.database[action_name] = new_action

	def get_stats(self):
		"""
		Creates a string formatted json object of all actions in self.database, along with the average time.

		:return: string formatted json object
		"""

		stats = []

		with self.lock.r_locked():
			for action_name in self.database:
				action = self.database[action_name]
				new_item = {
					"action": action_name,
					"avg": action.get_average()
				}
				stats.append(new_item)

		return json.dumps(stats)
