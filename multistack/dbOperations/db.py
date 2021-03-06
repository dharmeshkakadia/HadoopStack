import os
import multistack
from time import sleep

def get_node_objects(conn, role, resv_id=None):

	nodes = list()
	for resv in conn.get_all_instances():
		if resv.id == resv_id:
			for instance in resv.instances:
				node = dict()
				node['id'] = instance.id
				node['private_ip_address'] = instance.private_ip_address
				node['ip_address'] = instance.ip_address
				node['reservation_id'] = resv_id
				node['role'] = role
				node['flavor'] = instance.instance_type
				nodes.append(node)
	print nodes
	return nodes

def flush_data_to_mongo(db_name, data_dict):
	if db_name == 'job':
		multistack.main.mongo.db.job.save(data_dict)

	if db_name == 'conf':
		multistack.main.mongo.db.conf.save(data_dict)
