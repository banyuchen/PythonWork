from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    """
    规范化一个类,必须实现@abstractmethod装饰的方法。
    """
    @abstractmethod
    def pay(self, money):
        raise NotImplemented


class Wechat(Payment):
    def pay(self, money):
        print("微信支付了%s元"%money)


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付了%s"%money)


pay = Alipay()
