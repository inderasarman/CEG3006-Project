Class RSU:
	def __init__(self):
		self.cam = camera()			# init camera object for pedestrian detection
		self.lidar = lidar()		# init lidar object for vehicle detection
		
		self.ps = pedestrianSafety()		# init pedestrianSafety object to control pedestrian safety system
		self.va = vehicleAdvisory()			# init vehicleAdvisory object to provide appropriate vehicle advisory
		
		self.vnu = vehicleNetworkUnit()		# init networking unit to handle vehicle communication

		self.logger = dataLoggerToBackend()	# init data logger to log to backend server

		self.pedestrian_flag = false		# init to false, no pedestrian detected
		self.set_safety(OFF)				# init to "OFF" safety

		self.threshold_config = create_default_config()		# Default threshold config, adjustable by RSU / road, specified in pseudo_code_rsu_threshold
		
		self.crossing_gps_coord = "1°23'51.2\"N 103°54'12.9\"E"	# init static coordinates of pedestrian crossing

	def set_threshold(self, spd, bdist, dist2c):
		# Configurable based on city planner/traffic designer requirements
		self.threshold_limits["speed"] = spd

		# some implementation 

	def set_safety(self, severity):
		if severity == OFF:
			self.ps.lights(OFF)
			self.ps.alarm(OFF)

		elif severity == AMBER:
			self.ps.lights(AMBER)
			self.ps.alarm(LOW)	// Soft & Slow beeping

		elif severity == RED:
			self.ps.lights(RED)
			self.ps.alarm(HIGH)	// Louder & Faster beeping

	def detect_pedestrian(self):
		# camera uses computer vision to scan for objects in surroundings,
		# identified objects have their names added to an array, camera_vision_objects
		cam.get_camera_objects()

		if "elderly" in cam.camera_vision_objects:
			self.config.activate_enhanced_threshold()
		else:
			self.config.deactivate_enhanced_threshold()

		if "person" in cam.camera_vision_objects:
			self.pedestrian_flag = true
			# Start logger to log data
			self.logger.start_logger()
		else:
			self.pedestrian_flag = false
			# Stop logger
			self.logger.stop_logger()

	def start_advertise(self):
		# begins advertising on network with included GPS coordinate of pedestrian crossing
		self.vnu.start()
		
		# handles new thread for each new connection to each vehicle
		# thread tracks its own vehicle in self.vnu.vehicles, holding all vehicles
		# config used to evaluate alert to from crossing_decision()
		# crossing_gps_coord used to calculate distance to crossing
		# logger used to send logs
		self.vnu.register_connection_handler()
		
	def get_vehicle_info(self):
		# After each vehicle joins the service, this function is used for RSU to get vehicle details, collectively stored in self.vnu.vehicles
		self.vnu.request(vehicle_info_get_request)

	def send_vehicle_advisory(self, vehicle_id, decision_result):
		# After each vehicle joins the service, this function is used by RSU to send vehicle safety advisories, collectively stored in self.vnu.vehicles
		self.vnu.vehicle_respond(vehicle_id, decision_result)

	def set_safety_level(self):
		# function to warn pedestrians

		# turn off safety when no vehicles
		if not self.vnu.vehicles:
			set_safety(OFF)
			return

		# safety level is accessed and updated by each vnu connection thread
		set_safety(self.vnu.safety_level)


if __name__ == "__main__":
	# initialises RSU
	myRSU = RSU()

	while true:
		myRSU.detect_pedestrian()

		if myRSU.pedestrian_flag == true:
			myRSU.start_advertise()
			myRSU.get_vehicle_info()
			myRSU.set_safety_level()
		else:
			myRSU.stop_advertise()
			myRSU_set_safety(OFF)
