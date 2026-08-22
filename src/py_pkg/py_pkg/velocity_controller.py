class VelocityController(Node):
    def __init__(self):
        super().__init__('velocity_controller')

        self.kp = 1.5
        self.ki = 0.3

        self.v_ref = 0.0
        self.v = 0.0
        self.integral = 0.0

        self.last_time = self.get_clock().now()

        self.create_subscription(Float64, '/velocity_ref', self.ref_cb, 10)
        self.create_subscription(Odometry, '/odom', self.odom_cb, 10)
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

        self.create_timer(0.05, self.control_loop)  # 20 Hz

    def ref_cb(self, msg):
        self.v_ref = msg.data

    def odom_cb(self, msg):
        self.v = msg.twist.twist.linear.x

    def control_loop(self):
        now = self.get_clock().now()
        dt = (now - self.last_time).nanoseconds * 1e-9
        self.last_time = now

        error = self.v_ref - self.v
        self.integral += error * dt

        u = self.kp * error + self.ki * self.integral

        cmd = Twist()
        cmd.linear.x = max(min(u, 1.0), -1.0)  # saturação
        self.pub.publish(cmd)
