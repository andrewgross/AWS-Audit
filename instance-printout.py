import boto
import boto.ec2

def print_volume_info_by_id(volumeId):
    for volume in volumes:
        if volume.id == volumeId:
            for tag in volume.tags.keys():
                print "    %s: %s" % (tag, volume.tags[tag])
            print "    Mount Point: ", volume.attach_data.device
            print "    Size: ", volume.size
            print "    -----"



conn = boto.connect_ec2()
reservations = conn.get_all_instances()
volumes = conn.get_all_volumes()

for reservation in reservations:
    for instance in reservation.instances:
        if instance.state != "running":
            continue
        for tag in instance.tags.keys():
            print "%s: %s" % (tag, instance.tags[tag])
        #print "Instance ID: ", instance.id
        #print "Keypair: ", instance.key_name
        print "Instance Type: ", instance.instance_type
        print "IP Address: ", instance.private_ip_address
        print "Volumes: "
        for key in instance.block_device_mapping.keys():
            print_volume_info_by_id(instance.block_device_mapping[key].volume_id)

        
            


