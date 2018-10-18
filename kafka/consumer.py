# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:07:04 2018

@author: admin
"""

from pykafka import KafkaClient


class Kafka_client(object):
    def __init__(self, host="172.18.19.156:9092"):
        self.host = host
        self.client = KafkaClient(hosts=self.host)

    def simple_consumer(self, offset=0):
        """
        消费者指定消费
        :param offset:
        :return:
        """

        topic = self.client.topics["report_in_queue".encode()]
        partitions = topic.partitions
        last_offset = topic.latest_available_offsets()
        print("最近可用offset {}".format(last_offset))  # 查看所有分区
        consumer = topic.get_simple_consumer(b"simple_consumer_group", partitions=[partitions[0]])  # 选择一个分区进行消费
        offset_list = consumer.held_offsets
        print("当前消费者分区offset情况{}".format(offset_list))  # 消费者拥有的分区offset的情况
        consumer.reset_offsets([(partitions[0], offset)])  # 设置offset
        msg = consumer.consume()
        print("消费 :{}".format(msg.value.decode()))
        msg = consumer.consume()
        print("消费 :{}".format(msg.value.decode()))
        msg = consumer.consume()
        print("消费 :{}".format(msg.value.decode()))
        offset = consumer.held_offsets
        print("当前消费者分区offset情况{}".format(offset)) # 3

    def balance_consumer(self, offset=0):
        """
        使用balance consumer去消费kafka
        :return:
        """
        topic = self.client.topics["report_in_queue".encode()]
        # managed=True 设置后，使用新式reblance分区方法，不需要使用zk，而False是通过zk来实现reblance的需要使用zk
        consumer = topic.get_balanced_consumer(b"report_in_queue", managed=True)
        partitions = topic.partitions
        print("分区 {}".format(partitions))
        earliest_offsets = topic.earliest_available_offsets()
        print("最早可用offset {}".format(earliest_offsets))
        last_offsets = topic.latest_available_offsets()
        print("最近可用offset {}".format(last_offsets))
        offset = consumer.held_offsets
        print("当前消费者分区offset情况{}".format(offset))
        while True:
            msg = consumer.consume()
            offset = consumer.held_offsets
            print("{}, 当前消费者分区offset情况{}".format(msg.value.decode(), offset))

if __name__ == '__main__':
    kafka_ins = Kafka_client()
#    kafka_ins.simple_consumer()
    kafka_ins.balance_consumer()