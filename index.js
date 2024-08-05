let root = document.getElementById('root')
let sorted = document.getElementById('sorted')


function fetchData(){
    fetch('./data.json')
        .then((res) =>{
            if (!res.ok){
                throw new Error
                    ('error: Status: ${res.status}');
            }
            return res.json();
        })
        .then((data) => {
            let position = 1
            const sortedData = [...data].sort((a, b) => b.rating - a.rating)

            const positionMap = {};
            sortedData.forEach((element, index) => {
                // Verifica se a posição já foi atribuída ao mesmo rating
                if (positionMap[element.rating] === undefined) {
                    positionMap[element.rating] = index + 1;
                }
            });

            const dataWithPosition = data.map(element => ({
                ...element,
                position: positionMap[element.rating]
            }));

            dataWithPosition.sort((a, b) => a.name.localeCompare(b.name));

            dataWithPosition.forEach(element => root.insertAdjacentHTML('beforebegin', 
                `<tr class="hover:bg-zinc-800 hover:text-zinc-100">
                    <td class="text-zinc-500 p-2">${element.position}°</td>
                    <td class="text-zinc-500 p-2">${element.name}</td>
                    <td  class="text-zinc-500">${element.rating}</td>
                </tr>`));        }
        )
        .catch((error) => 
            console.error("Nao achei"));
}
function fetchData2(){
    let position = 1
    fetch('./data.json')
        .then((res) =>{
            if (!res.ok){
                throw new Error
                    ('error: Status: ${res.status}');
            }
            return res.json();
        })
        .then((data) => {
            data.sort((a, b) => b.rating - a.rating)
            data.forEach(element => sorted.insertAdjacentHTML(
                'beforebegin', 
                `<tr class="hover:bg-zinc-800 hover:text-zinc-100">
                    <td class="text-zinc-500 p-2">${position++}°</td>
                    <td class="text-zinc-500 p-2">${element.name}</td>
                    <td  class="text-zinc-500">${element.rating}</td>
                    </tr>`));        }
        )
        .catch((error) => 
            console.error("Nao achei"));
    }
fetchData()
fetchData2()
