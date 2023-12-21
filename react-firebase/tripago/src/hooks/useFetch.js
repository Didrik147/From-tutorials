import { useState, useEffect } from 'react'

export const useFetch = (url) => {
  const [data, setData] = useState(null)
  const [isPending, setIsPending] = useState(false)

  useEffect(() => {
    const fetchData = async () => {
      setIsPending(true)

      const res = await fetch(url)
      const json = await res.json()
      
      setIsPending(false)
      
      setData(json)
    }

    fetchData()

  }, [url])

  return { data, isPending }
}
