from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        SERVICE_TYPES = ["MainService","SecondaryService"]
        if service_type not in SERVICE_TYPES:
            raise Exception("Invalid service type!")

        if service_type == SERVICE_TYPES[0]:
            service = MainService(name)
        if service_type == SERVICE_TYPES[1]:
            service = SecondaryService(name)

        self.services.append(service)
        return f"{service_type} is successfully added."


    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        valid_robot_types = ["MaleRobot", "FemaleRobot"]
        if robot_type not in valid_robot_types:
            raise Exception("Invalid robot type!")

        if robot_type == valid_robot_types[0]:
            robot = MaleRobot(name, kind, price)
        if robot_type == valid_robot_types[1]:
            robot = FemaleRobot(name, kind, price)

        self.robots.append(robot)
        return f"{robot_type} is successfully added."


    def add_robot_to_service(self, robot_name: str, service_name: str):
        target_robot = [robot for robot in self.robots if robot_name == robot.name][0]
        robot_type = type(target_robot).__name__

        if (robot_type == "FemaleRobot" and service_name == "MainService") \
                or robot_type == "MaleRobot" and service_name == "SecondaryService":
            return "Unsuitable service."

        target_service = [service for service in self.services if service_name == service.name][0]
        service_type = type(target_service).__name__

        if service_type == "MainService" and len(target_service.robots) == 30:
            raise Exception("Not enough capacity for this robot!")
        if service_type == "SecondaryService" and len(target_service.robots) == 15:
            raise Exception("Not enough capacity for this robot!")

        target_service.robots.append(target_robot)
        self.robots.remove(target_robot)

        return f"Successfully added {robot_name} to {service_name}."


    def remove_robot_from_service(self, robot_name: str, service_name: str):
        target_service = [service for service in self.services if service_name == service.name][0]
        if robot_name not in [robot.name for robot in target_service.robots]:
            raise Exception("No such robot in this service!")
        target_robot = [robot for robot in target_service.robots if robot_name == robot.name][0]
        target_service.robots.remove(target_robot)
        self.robots.append(target_robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        target_service = [service for service in self.services if service_name == service.name][0]
        for robot in target_service.robots:
            robot.eating()
        return f"Robots fed: {len(target_service.robots)}."

    def service_price(self, service_name: str):
        total_price = 0
        target_service = [service for service in self.services if service_name == service.name][0]
        for robot in target_service.robots:
            total_price += robot.price
        return f"The value of service {service_name} is {total_price}."


    def __str__(self):
        for service in self.services:
            return service.details()