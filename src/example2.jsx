import {Header} from './header';
import {useImmer} from './library';
import React from 'react';

function Example2() {
  const [books, setBooks] = useImmer([
      {id: 1, is_open: true, price: 100},
      {id: 2, is_open: false, price: 200},
      {id: 3, is_open: true, price: 300},
    ])
  const [idCounter, setIdCounter] = React.useState(4)

  const open = function(book_index) {
    setBooks(draft => {
      draft[book_index].is_open = true
    })
  }

  const close = function(book_index) {
    setBooks(draft => {
      draft[book_index].is_open = false
    })
  }

  const add = function() {
    setBooks(draft => {
      draft.push({id: idCounter, is_open: false, price: 80})
    })
    setIdCounter(idCounter + 1)
  }

  const increase_price = function(book_index, price) {
    setBooks(draft => {
      draft[book_index].price += price
    })
  }

  return (
    <div >
      <Header/>
      <h2>Example2</h2>
      <div className="top_box" >
        {books.map((book, book_index) => (
          <div key={book.id} style={{border: "solid red 1px", padding: "10px"}} >
            Book-{book.id}
            <div>{book.is_open ? "Open" : "Close"} ; Price = {book.price}</div>
            <button onClick={() => open(book_index)} >Open</button>
            <button onClick={() => close(book_index)} >Close</button>
            <button onClick={() => increase_price(book_index, 100)} >
              Increase Price
            </button>
          </div>
        ))}
      </div>
      <button onClick={add} >Add</button>
    </div>
  );
}

export default Example2;
