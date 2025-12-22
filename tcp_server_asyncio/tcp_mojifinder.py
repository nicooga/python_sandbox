import asyncio

from misc.emojiindex import EmojiInvertedIndex

async def supervisor(host, port) -> None:
    server = await asyncio.start_server(
        finder,
        host,
        port
    )

    addr = server.sockets[0].getsockname()

    print(f'Listening on {addr}')

    try:
        await server.serve_forever()
    except asyncio.CancelledError:
        print('Received cancellation signal. Shutting down...')
    finally:
        server.close()
        await server.wait_closed()

PROMPT = '?> '

async def finder(
    reader: asyncio.StreamReader,
    writer: asyncio.StreamWriter
) -> None:
    index = EmojiInvertedIndex()
    client_address = writer.get_extra_info('peername')

    try:
        while True:
            writer.write(PROMPT.encode())
            await writer.drain()

            try:
                line = await reader.readline()
                if not line: break
                query = line.decode().strip()
            except UnicodeDecodeError:
                print(f'From {client_address}: Invalid query')
                break

            if not query: continue

            print(f'From {client_address}: {query}')

            emojis = index.search(query)
            response = f'{len(emojis)} emojis found\n'
            response += ''.join(emojis) + '\n'

            writer.write(response.encode())
            await writer.drain()
    except (ConnectionError, OSError) as e:
        print(f'From {client_address}: Connection error: {e}')
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == '__main__':
    asyncio.run(supervisor('127.0.0.1', 8000))

