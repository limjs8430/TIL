### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
select * from playlist_track as 'A' order by PlaylistId desc limit 5;
```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
select * from tracks as 'B' order by TrackId limit 5;

``` 
 
### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 
```sql
select A.playlistId, B.Name from playlist_track as 'A' join tracks as 'B' on A.TrackId = B.TrackId order by A.playlistId desc limit 10;
```  

### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
select A.playlistId, B.Name from playlist_track as 'A' join tracks as 'B' on A.TrackId = B.TrackId where A.playlistId = 10 order by B.Name desc limit 5;
``` 

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
select count(*) from tracks as 'a' join artists as 'b' on a.Composer = b.Name;
```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
select count(*) from tracks as 'a' left join artists as 'b' on a.Composer = b.Name;
```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
이너조인은 교집합이여서 null값은 제외되지만 레프트 아우터 조인은 널값에 있는 데이터도 포함되서 갯수가 차이납니다.
```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
select InvoiceLineId, InvoiceId from invoice_items order by InvoiceId limit 5;
``` 

### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
select InvoiceId, CustomerId from invoices order by InvoiceId limit 5;
``` 

### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
select InvoiceLineId, InvoiceId from invoice_items order by InvoiceId desc limit 5;
``` 


### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
select InvoiceId, CustomerId from invoices order by InvoiceId desc limit 5;
``` 

### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
select a.InvoiceLineId, a.InvoiceId, b.CustomerId from invoice_items as 'a' join invoices as 'b' on a.InvoiceId = b.InvoiceId order by a.InvoiceId desc limit 5;
```

### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
select b.CustomerId, count(*) from invoice_items as 'a' join invoices as 'b' on a.InvoiceId = b.InvoiceId group by b.CustomerId order by b.CustomerId limit 5;
``` 

