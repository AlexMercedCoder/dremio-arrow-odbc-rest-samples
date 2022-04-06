```
SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
ERROR StatusLogger Log4j2 could not find a logging implementation. Please add log4j-core to the classpath. Using SimpleLogger to log to the console...
Traceback (most recent call last):
  File "Thread.java", line 833, in java.lang.Thread.run
  File "ThreadExecutorMap.java", line 74, in cdjd.io.netty.util.internal.ThreadExecutorMap$2.run
  File "SingleThreadEventExecutor.java", line 989, in cdjd.io.netty.util.concurrent.SingleThreadEventExecutor$4.run
  File "NioEventLoop.java", line 493, in cdjd.io.netty.channel.nio.NioEventLoop.run
  File "NioEventLoop.java", line 576, in cdjd.io.netty.channel.nio.NioEventLoop.processSelectedKeys
  File "NioEventLoop.java", line 650, in cdjd.io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized
  File "NioEventLoop.java", line 702, in cdjd.io.netty.channel.nio.NioEventLoop.processSelectedKey
  File "AbstractNioChannel.java", line 335, in cdjd.io.netty.channel.nio.AbstractNioChannel$AbstractNioUnsafe.finishConnect
  File "AbstractNioChannel.java", line 300, in cdjd.io.netty.channel.nio.AbstractNioChannel$AbstractNioUnsafe.fulfillConnectPromise
  File "DefaultChannelPromise.java", line 84, in cdjd.io.netty.channel.DefaultChannelPromise.trySuccess
  File "DefaultPromise.java", line 104, in cdjd.io.netty.util.concurrent.DefaultPromise.trySuccess
  File "DefaultPromise.java", line 604, in cdjd.io.netty.util.concurrent.DefaultPromise.setSuccess0
  File "DefaultPromise.java", line 615, in cdjd.io.netty.util.concurrent.DefaultPromise.setValue0
  File "DefaultPromise.java", line 490, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListeners
  File "DefaultPromise.java", line 549, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListenersNow
  File "DefaultPromise.java", line 570, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListeners0
  File "DefaultPromise.java", line 577, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListener0
  File "BasicClient.java", line 272, in cdjd.com.dremio.exec.rpc.BasicClient$ConnectionMultiListener$ConnectionEstablishmentListener.operationComplete
  File "BasicClient.java", line 291, in cdjd.com.dremio.exec.rpc.BasicClient$ConnectionMultiListener$ConnectionEstablishmentListener.operationComplete
  File "BasicClient.java", line 350, in cdjd.com.dremio.exec.rpc.BasicClient$ConnectionMultiListener$ConnectionEstablishmentListener.addNegotiator
  File "DefaultChannelPipeline.java", line 152, in cdjd.io.netty.channel.DefaultChannelPipeline.addFirst
  File "DefaultChannelPipeline.java", line 181, in cdjd.io.netty.channel.DefaultChannelPipeline.addFirst
  File "DefaultChannelPipeline.java", line 609, in cdjd.io.netty.channel.DefaultChannelPipeline.callHandlerAdded0
  File "AbstractChannelHandlerContext.java", line 971, in cdjd.io.netty.channel.AbstractChannelHandlerContext.callHandlerAdded
  File "SslHandler.java", line 1903, in cdjd.io.netty.handler.ssl.SslHandler.handlerAdded
  File "SslHandler.java", line 1914, in cdjd.io.netty.handler.ssl.SslHandler.startHandshakeProcessing
  File "SslHandler.java", line 1994, in cdjd.io.netty.handler.ssl.SslHandler.handshake
  File "SslHandler.java", line 943, in cdjd.io.netty.handler.ssl.SslHandler.wrapNonAppData
  File "SslHandler.java", line 1051, in cdjd.io.netty.handler.ssl.SslHandler.wrap
  File "NettyArrowBuf.java", line 238, in cdjd.io.netty.buffer.NettyArrowBuf.nioBuffer
  File "NettyArrowBuf.java", line 260, in cdjd.io.netty.buffer.NettyArrowBuf.getDirectBuffer
  File "PlatformDependent.java", line 490, in cdjd.io.netty.util.internal.PlatformDependent.directBuffer
java.lang.UnsupportedOperationException: java.lang.UnsupportedOperationException: sun.misc.Unsafe or java.nio.DirectByteBuffer.<init>(long, int) not available

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "Thread.java", line 833, in java.lang.Thread.run
  File "ThreadExecutorMap.java", line 74, in cdjd.io.netty.util.internal.ThreadExecutorMap$2.run
  File "SingleThreadEventExecutor.java", line 989, in cdjd.io.netty.util.concurrent.SingleThreadEventExecutor$4.run
  File "NioEventLoop.java", line 493, in cdjd.io.netty.channel.nio.NioEventLoop.run
  File "NioEventLoop.java", line 576, in cdjd.io.netty.channel.nio.NioEventLoop.processSelectedKeys
  File "NioEventLoop.java", line 650, in cdjd.io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized
  File "NioEventLoop.java", line 702, in cdjd.io.netty.channel.nio.NioEventLoop.processSelectedKey
  File "AbstractNioChannel.java", line 335, in cdjd.io.netty.channel.nio.AbstractNioChannel$AbstractNioUnsafe.finishConnect
  File "AbstractNioChannel.java", line 300, in cdjd.io.netty.channel.nio.AbstractNioChannel$AbstractNioUnsafe.fulfillConnectPromise
  File "DefaultChannelPromise.java", line 84, in cdjd.io.netty.channel.DefaultChannelPromise.trySuccess
  File "DefaultPromise.java", line 104, in cdjd.io.netty.util.concurrent.DefaultPromise.trySuccess
  File "DefaultPromise.java", line 604, in cdjd.io.netty.util.concurrent.DefaultPromise.setSuccess0
  File "DefaultPromise.java", line 615, in cdjd.io.netty.util.concurrent.DefaultPromise.setValue0
  File "DefaultPromise.java", line 490, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListeners
  File "DefaultPromise.java", line 549, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListenersNow
  File "DefaultPromise.java", line 570, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListeners0
  File "DefaultPromise.java", line 577, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListener0
  File "BasicClient.java", line 272, in cdjd.com.dremio.exec.rpc.BasicClient$ConnectionMultiListener$ConnectionEstablishmentListener.operationComplete
  File "BasicClient.java", line 291, in cdjd.com.dremio.exec.rpc.BasicClient$ConnectionMultiListener$ConnectionEstablishmentListener.operationComplete
  File "BasicClient.java", line 350, in cdjd.com.dremio.exec.rpc.BasicClient$ConnectionMultiListener$ConnectionEstablishmentListener.addNegotiator
  File "DefaultChannelPipeline.java", line 152, in cdjd.io.netty.channel.DefaultChannelPipeline.addFirst
  File "DefaultChannelPipeline.java", line 181, in cdjd.io.netty.channel.DefaultChannelPipeline.addFirst
  File "DefaultChannelPipeline.java", line 609, in cdjd.io.netty.channel.DefaultChannelPipeline.callHandlerAdded0
  File "AbstractChannelHandlerContext.java", line 971, in cdjd.io.netty.channel.AbstractChannelHandlerContext.callHandlerAdded
  File "SslHandler.java", line 1903, in cdjd.io.netty.handler.ssl.SslHandler.handlerAdded
  File "SslHandler.java", line 1914, in cdjd.io.netty.handler.ssl.SslHandler.startHandshakeProcessing
  File "SslHandler.java", line 1996, in cdjd.io.netty.handler.ssl.SslHandler.handshake
  File "SslHandler.java", line 1773, in cdjd.io.netty.handler.ssl.SslHandler.setHandshakeFailure
  File "SslHandler.java", line 1804, in cdjd.io.netty.handler.ssl.SslHandler.setHandshakeFailure
  File "DefaultPromise.java", line 117, in cdjd.io.netty.util.concurrent.DefaultPromise.tryFailure
  File "DefaultPromise.java", line 608, in cdjd.io.netty.util.concurrent.DefaultPromise.setFailure0
  File "DefaultPromise.java", line 615, in cdjd.io.netty.util.concurrent.DefaultPromise.setValue0
  File "DefaultPromise.java", line 490, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListeners
  File "DefaultPromise.java", line 551, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListenersNow
  File "DefaultPromise.java", line 577, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListener0
  File "BasicClient.java", line 342, in cdjd.com.dremio.exec.rpc.BasicClient$ConnectionMultiListener$ConnectionEstablishmentListener.lambda$addNegotiator$0
cdjd.com.dremio.exec.rpc.RpcException: cdjd.com.dremio.exec.rpc.RpcException: SSL negotiation failed

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "Thread.java", line 833, in java.lang.Thread.run
  File "ThreadExecutorMap.java", line 74, in cdjd.io.netty.util.internal.ThreadExecutorMap$2.run
  File "SingleThreadEventExecutor.java", line 989, in cdjd.io.netty.util.concurrent.SingleThreadEventExecutor$4.run
  File "NioEventLoop.java", line 493, in cdjd.io.netty.channel.nio.NioEventLoop.run
  File "NioEventLoop.java", line 576, in cdjd.io.netty.channel.nio.NioEventLoop.processSelectedKeys
  File "NioEventLoop.java", line 650, in cdjd.io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized
  File "NioEventLoop.java", line 702, in cdjd.io.netty.channel.nio.NioEventLoop.processSelectedKey
  File "AbstractNioChannel.java", line 335, in cdjd.io.netty.channel.nio.AbstractNioChannel$AbstractNioUnsafe.finishConnect
  File "AbstractNioChannel.java", line 300, in cdjd.io.netty.channel.nio.AbstractNioChannel$AbstractNioUnsafe.fulfillConnectPromise
  File "DefaultChannelPromise.java", line 84, in cdjd.io.netty.channel.DefaultChannelPromise.trySuccess
  File "DefaultPromise.java", line 104, in cdjd.io.netty.util.concurrent.DefaultPromise.trySuccess
  File "DefaultPromise.java", line 604, in cdjd.io.netty.util.concurrent.DefaultPromise.setSuccess0
  File "DefaultPromise.java", line 615, in cdjd.io.netty.util.concurrent.DefaultPromise.setValue0
  File "DefaultPromise.java", line 490, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListeners
  File "DefaultPromise.java", line 549, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListenersNow
  File "DefaultPromise.java", line 570, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListeners0
  File "DefaultPromise.java", line 577, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListener0
  File "BasicClient.java", line 272, in cdjd.com.dremio.exec.rpc.BasicClient$ConnectionMultiListener$ConnectionEstablishmentListener.operationComplete
  File "BasicClient.java", line 291, in cdjd.com.dremio.exec.rpc.BasicClient$ConnectionMultiListener$ConnectionEstablishmentListener.operationComplete
  File "BasicClient.java", line 350, in cdjd.com.dremio.exec.rpc.BasicClient$ConnectionMultiListener$ConnectionEstablishmentListener.addNegotiator
  File "DefaultChannelPipeline.java", line 152, in cdjd.io.netty.channel.DefaultChannelPipeline.addFirst
  File "DefaultChannelPipeline.java", line 181, in cdjd.io.netty.channel.DefaultChannelPipeline.addFirst
  File "DefaultChannelPipeline.java", line 609, in cdjd.io.netty.channel.DefaultChannelPipeline.callHandlerAdded0
  File "AbstractChannelHandlerContext.java", line 971, in cdjd.io.netty.channel.AbstractChannelHandlerContext.callHandlerAdded
  File "SslHandler.java", line 1903, in cdjd.io.netty.handler.ssl.SslHandler.handlerAdded
  File "SslHandler.java", line 1914, in cdjd.io.netty.handler.ssl.SslHandler.startHandshakeProcessing
  File "SslHandler.java", line 1996, in cdjd.io.netty.handler.ssl.SslHandler.handshake
  File "SslHandler.java", line 1773, in cdjd.io.netty.handler.ssl.SslHandler.setHandshakeFailure
  File "SslHandler.java", line 1804, in cdjd.io.netty.handler.ssl.SslHandler.setHandshakeFailure
  File "DefaultPromise.java", line 117, in cdjd.io.netty.util.concurrent.DefaultPromise.tryFailure
  File "DefaultPromise.java", line 608, in cdjd.io.netty.util.concurrent.DefaultPromise.setFailure0
  File "DefaultPromise.java", line 615, in cdjd.io.netty.util.concurrent.DefaultPromise.setValue0
  File "DefaultPromise.java", line 490, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListeners
  File "DefaultPromise.java", line 551, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListenersNow
  File "DefaultPromise.java", line 577, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListener0
  File "BasicClient.java", line 341, in cdjd.com.dremio.exec.rpc.BasicClient$ConnectionMultiListener$ConnectionEstablishmentListener.lambda$addNegotiator$0
  File "QueryResultHandler.java", line 387, in cdjd.com.dremio.sabot.rpc.user.QueryResultHandler$ChannelClosedHandler.connectionFailed
  File "DremioClient.java", line 825, in cdjd.com.dremio.exec.client.DremioClient$FutureHandler.connectionFailed
cdjd.com.dremio.exec.rpc.RpcException: cdjd.com.dremio.exec.rpc.RpcException: CONNECTION : SSL negotiation failed

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "Thread.java", line 833, in java.lang.Thread.run
  File "ThreadExecutorMap.java", line 74, in cdjd.io.netty.util.internal.ThreadExecutorMap$2.run
  File "SingleThreadEventExecutor.java", line 989, in cdjd.io.netty.util.concurrent.SingleThreadEventExecutor$4.run
  File "NioEventLoop.java", line 493, in cdjd.io.netty.channel.nio.NioEventLoop.run
  File "NioEventLoop.java", line 576, in cdjd.io.netty.channel.nio.NioEventLoop.processSelectedKeys
  File "NioEventLoop.java", line 650, in cdjd.io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized
  File "NioEventLoop.java", line 702, in cdjd.io.netty.channel.nio.NioEventLoop.processSelectedKey
  File "AbstractNioChannel.java", line 335, in cdjd.io.netty.channel.nio.AbstractNioChannel$AbstractNioUnsafe.finishConnect
  File "AbstractNioChannel.java", line 300, in cdjd.io.netty.channel.nio.AbstractNioChannel$AbstractNioUnsafe.fulfillConnectPromise
  File "DefaultChannelPromise.java", line 84, in cdjd.io.netty.channel.DefaultChannelPromise.trySuccess
  File "DefaultPromise.java", line 104, in cdjd.io.netty.util.concurrent.DefaultPromise.trySuccess
  File "DefaultPromise.java", line 604, in cdjd.io.netty.util.concurrent.DefaultPromise.setSuccess0
  File "DefaultPromise.java", line 615, in cdjd.io.netty.util.concurrent.DefaultPromise.setValue0
  File "DefaultPromise.java", line 490, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListeners
  File "DefaultPromise.java", line 549, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListenersNow
  File "DefaultPromise.java", line 570, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListeners0
  File "DefaultPromise.java", line 577, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListener0
  File "BasicClient.java", line 272, in cdjd.com.dremio.exec.rpc.BasicClient$ConnectionMultiListener$ConnectionEstablishmentListener.operationComplete
  File "BasicClient.java", line 291, in cdjd.com.dremio.exec.rpc.BasicClient$ConnectionMultiListener$ConnectionEstablishmentListener.operationComplete
  File "BasicClient.java", line 350, in cdjd.com.dremio.exec.rpc.BasicClient$ConnectionMultiListener$ConnectionEstablishmentListener.addNegotiator
  File "DefaultChannelPipeline.java", line 152, in cdjd.io.netty.channel.DefaultChannelPipeline.addFirst
  File "DefaultChannelPipeline.java", line 181, in cdjd.io.netty.channel.DefaultChannelPipeline.addFirst
  File "DefaultChannelPipeline.java", line 609, in cdjd.io.netty.channel.DefaultChannelPipeline.callHandlerAdded0
  File "AbstractChannelHandlerContext.java", line 971, in cdjd.io.netty.channel.AbstractChannelHandlerContext.callHandlerAdded
  File "SslHandler.java", line 1903, in cdjd.io.netty.handler.ssl.SslHandler.handlerAdded
  File "SslHandler.java", line 1914, in cdjd.io.netty.handler.ssl.SslHandler.startHandshakeProcessing
  File "SslHandler.java", line 1996, in cdjd.io.netty.handler.ssl.SslHandler.handshake
  File "SslHandler.java", line 1773, in cdjd.io.netty.handler.ssl.SslHandler.setHandshakeFailure
  File "SslHandler.java", line 1804, in cdjd.io.netty.handler.ssl.SslHandler.setHandshakeFailure
  File "DefaultPromise.java", line 117, in cdjd.io.netty.util.concurrent.DefaultPromise.tryFailure
  File "DefaultPromise.java", line 608, in cdjd.io.netty.util.concurrent.DefaultPromise.setFailure0
  File "DefaultPromise.java", line 615, in cdjd.io.netty.util.concurrent.DefaultPromise.setValue0
  File "DefaultPromise.java", line 490, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListeners
  File "DefaultPromise.java", line 551, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListenersNow
  File "DefaultPromise.java", line 577, in cdjd.io.netty.util.concurrent.DefaultPromise.notifyListener0
  File "BasicClient.java", line 341, in cdjd.com.dremio.exec.rpc.BasicClient$ConnectionMultiListener$ConnectionEstablishmentListener.lambda$addNegotiator$0
  File "QueryResultHandler.java", line 387, in cdjd.com.dremio.sabot.rpc.user.QueryResultHandler$ChannelClosedHandler.connectionFailed
  File "DremioClient.java", line 829, in cdjd.com.dremio.exec.client.DremioClient$FutureHandler.connectionFailed
  File "ConnectionFailedException.java", line 31, in cdjd.com.dremio.exec.rpc.ConnectionFailedException.mapException
cdjd.com.dremio.exec.rpc.ConnectionFailedException: cdjd.com.dremio.exec.rpc.ConnectionFailedException: CONNECTION : SSL negotiation failed

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "org.jpype.JPypeContext.java", line -1, in org.jpype.JPypeContext.callMethod
  File "Method.java", line 568, in java.lang.reflect.Method.invoke
  File "DelegatingMethodAccessorImpl.java", line 43, in jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke
  File "NativeMethodAccessorImpl.java", line 77, in jdk.internal.reflect.NativeMethodAccessorImpl.invoke
  File "NativeMethodAccessorImpl.java", line -2, in jdk.internal.reflect.NativeMethodAccessorImpl.invoke0
  File "DriverManager.java", line 252, in java.sql.DriverManager.getConnection
  File "DriverManager.java", line 681, in java.sql.DriverManager.getConnection
  File "Driver.java", line 84, in com.dremio.jdbc.Driver.connect
  File "UnregisteredDriver.java", line 138, in cdjd.org.apache.calcite.avatica.UnregisteredDriver.connect
  File "DremioFactory.java", line 67, in com.dremio.jdbc.impl.DremioFactory.newConnection
  File "DremioJdbc41Factory.java", line 72, in com.dremio.jdbc.impl.DremioJdbc41Factory.newConnection
  File "DremioConnectionImpl.java", line 104, in com.dremio.jdbc.impl.DremioConnectionImpl.<init>
  File "DremioExceptionMapper.java", line 81, in com.dremio.jdbc.impl.DremioExceptionMapper.map
Exception: Java Exception

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/alexmerced/development/developmentwork/dremio/odbc-arrow-python/jdbc.py", line 17, in <module>
    conn = jaydebeapi.connect("com.dremio.jdbc.Driver",
  File "/home/alexmerced/development/developmentwork/dremio/odbc-arrow-python/venv/lib/python3.10/site-packages/jaydebeapi/__init__.py", line 412, in connect
    jconn = _jdbc_connect(jclassname, url, driver_args, jars, libs)
  File "/home/alexmerced/development/developmentwork/dremio/odbc-arrow-python/venv/lib/python3.10/site-packages/jaydebeapi/__init__.py", line 230, in _jdbc_connect_jpype
    return jpype.java.sql.DriverManager.getConnection(url, *dargs)
java.sql.SQLException: java.sql.SQLException: Failure in connecting to Dremio: cdjd.com.dremio.exec.rpc.ConnectionFailedException: CONNECTION : SSL negotiation failed
```