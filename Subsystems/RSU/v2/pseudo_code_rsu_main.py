Class RSU:
	def __init__(self):
		self.cam = camera()			# init camera object for pedestrian detection
		self.lidar = lidar()		# init lidar object for vehicle detection
		
		self.ps = pedestrianSafety()		# init pedestrianSafety object to control pedestrian safety system
		self.va = vehicleAdvisory()			# init vehicleAdvisory object to provide appropriate vehicle advisory
		
		self.vnu = vehicleNetworkUnit()		# init networking unit to handle vehicle communication

		self.pedestrian_flag = false		# init to false, no pedestrian detected
		self.set_safety(OFF)				# init to "OFF" safety

		self.threshold_limits = {		# init placeholder for configurable limits
			"speed": 0 ,
			"braking_dist": 0,
			"dist_to_cross": 0
		}

		self.crossing_gps_coord = "1°23'51.2\"N 103°54'12.9\"E"	# init static coordinates of pedestrian crossing

	def set_threshold(self, spd, bdist, dist2c):
		# Configurable based on city planner/traffic designer requirements
		self.threshold_limits["speed"] = spd

		# some implementation 

	def set_safety(self, severity, ):
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

		if ("person" in cam.camera_vision_objects):
			self.pedestrian_flag = true
		else:
			self.pedestrian_flag = false

	def start_advertise(self):
		# begins advertising on network with included GPS coordinate of pedestrian crossing
		self.vnu.start(self.crossing_gps_coord)
		
		# Starts new thread for new connection to each vehicle
		# thread tracks its own vehicle in self.vnu.vehicles, holding all vehicles
		self.vnu.register_connection_handler()
		
	def get_vehicle_info(self):
		# After vehicle joins the service, this function is called to get vehicle details, stored in self.vnu.vehicles
		self.vnu.request(vehicle_info_get_request)

	def set_safety_level(self):
		if not self.vnu.vehicles:
			set_safety(OFF)
			return
			
		for veh_id, vehicle in self.vnu.vehicles.items():
			if (vehicle["speed"] >= self.threshold_limits["speed"] OR
			   vehicle["braking_dist"] >= self.threshold_limits["braking_dist"]) AND
			   vehicle["dist_to_cross"] <= self.threshold_limits["dist_to_cross"]:
				set_safety(RED)
				break
			else:
				set_safety(AMBER)


if __name__ == "__main__":
	# initialises RSU
	myRSU = RSU()

	myRSU.start_advertise()
	myRSU.set_threshold(40, 10, 50)	# in kmph, meter, meter

	while true:
		myRSU.detect_pedestrian()

		if myRSU.pedestrian_flag == true:
			myRSU.get_vehicle_info()
			myRSU.set_safety_level()
		else:
			myRSU_set_safety(OFF)
